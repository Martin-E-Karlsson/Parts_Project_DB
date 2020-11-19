from model.db import session
from model.models.source import Source


def insert_source(manufacturer_id):
    new_source = Source(idManufacturer=manufacturer_id)
    session.add(new_source)
    session.commit()


def get_all_sources():
    return session.query(Source).all()


def get_source_by_manufacturer_id(manufacturer_id):
    return session.query(Source).filter(Source.idManufacturer == manufacturer_id).first()


def change_source_manufacturer_id(source, new_manufacturer_id):
    try:
        source.idManufacturer = new_manufacturer_id
        session.commit()
    except:
        session.rollback()
