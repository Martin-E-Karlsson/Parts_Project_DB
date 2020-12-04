import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from pymongo import MongoClient
from abc import ABC

from model.db.db_settings import *

engine = sqlalchemy.create_engine(
    f'mysql+mysqlconnector://{MYSQLDB_USER}:{MYSQLDB_PASSWORD}@{MYSQLDB_HOST}:{MYSQLDB_PORT}/{MYSQLDB_DATABASE}'
)

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

client = MongoClient(
    f'mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}'
)
db = client.model_db


class ResultList(list):
    def first_or_none(self):
        return self[0] if len(self) > 0 else None

    def last_or_none(self):
        return self[-1] if len(self) > 0 else None


class Document(dict, ABC):
    collection = None

    def __init__(self, data):
        super().__init__()
        if '_id' not in data:
            self._id = None
        self.__dict__.update(data)

    def __repr__(self):
        return '\n'.join(f'{k} = {v}' for k, v in self.__dict__.items())

    def save(self):
        if not self._id:
            del(self.__dict__['_id'])
            return self.collection.insert_one(self.__dict__)
        else:
            return self.collection.update({'_id': self._id}, **self.__dict__)

    def insert(self):
        return self.collection.insert_one(self.__dict__)

    @classmethod
    def insert_many(cls, items):
        for item in items:
            cls(item).save()

    @classmethod
    def all(cls):
        return [cls(item) for item in cls.collection.find({})]

    @classmethod
    def find(cls, **kwargs):
        return ResultList(cls(item) for item in cls.collection.find(kwargs))

    @classmethod
    def delete(cls, **kwargs):
        cls.collection.delete_many(kwargs)
