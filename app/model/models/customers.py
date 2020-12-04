from model.db import Document, db


class Customer(Document):
    collection = db.customers
