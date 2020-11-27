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


def get_all_retailers_by_attribute(attribute_name, value):
    try:
        return session.query(Retailer).filter(getattr(Retailer, attribute_name).like(f"%{value}%")).all()
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_retailer_attribute(retailer, attribute_name, new_value):
    try:
        setattr(retailer, attribute_name, new_value)
        session.commit()
    except ValueError:
        print('Incorrect argument entered')
        session.rollback()