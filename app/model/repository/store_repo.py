from model.db import session
from model.models.store import Store


def insert_store(name, store_type):
    new_store = Store(
        Name=name,
        StoreType=store_type
    )
    session.add(new_store)
    session.commit()


def get_all_stores():
    return session.query(Store).all()


def get_store_by_id(id_store):
    return session.query(Store).filter(Store.idStore == id_store).first()


def get_stores_by_name(name):
    return session.query(Store).filter(Store.Name.like(f"%{name}%")).all()


def get_stores_by_type(store_type):
    return session.query(Store).filter(Store.StoreType.like(f"%{store_type}%")).all()


def change_store_name(store, new_name):
    try:
        store.Name = new_name
        session.commit()
    except:
        session.rollback()


def change_store_type(store, new_type):
    try:
        store.StoreType = new_type
        session.commit()
    except:
        session.rollback()