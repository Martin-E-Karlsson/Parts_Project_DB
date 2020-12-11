from model.db import Document, db


class Product(Document):
    collection = db.products