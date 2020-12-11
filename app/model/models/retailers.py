from model.db import Document, db


class Retailer(Document):
    collection = db.retailers
