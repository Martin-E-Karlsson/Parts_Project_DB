from model.db import session
from model.models.retailer import Retailer


def insert_retailer(name, address, id_contact=None, id_manufacturer=None):
    new_retailer = Retailer(
        Name=name,
        Address=address,
        idContact=id_contact,
        idManufacturer=id_manufacturer
    )
    session.add(new_retailer)
    session.commit()


def get_all_retailers():
    return session.query(Retailer).all()


def get_retailer_by_id(id_retailer):
    return session.query(Retailer).filter(Retailer.idRetailer == id_retailer).first()


def get_retailer_by_name(name):
    return session.query(Retailer).filter(Retailer.Name.like(f"%{name}%").all())


def change_retailer_name(retailer, new_name):
    try:
        retailer.Name = new_name
        session.commit()
    except:
        session.rollback()