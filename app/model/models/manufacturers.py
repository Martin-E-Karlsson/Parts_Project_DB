from model.db import Document, db


class Manufacturer(Document):
    collection = db.manufacturers
