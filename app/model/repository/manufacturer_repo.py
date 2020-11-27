from model.db import session
from model.models.manufacturer import Manufacturer


def insert_manufacturer(hq_address, hq_phone_number, manufacturer_name):
    new_manufacturer = Manufacturer(
        HQAdress=hq_address,
        HQPhoneNumber=hq_phone_number,
        ManufacturerName=manufacturer_name
    )
    session.add(new_manufacturer)
    session.commit()


def get_all_manufacturers():
    return session.query(Manufacturer).all()


def get_manufacturer_by_id(id_manufacturer):
    return session.query(Manufacturer).filter(Manufacturer.idManufacturer == id_manufacturer).first()


def get_all_manufacturers_by_attribute(attribute_name, value):
    try:
        return session.query(Manufacturer).filter(getattr(Manufacturer, attribute_name).like(f"%{value}%")).all()
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_manufacturer_attribute(manufacturer, attribute_name, new_value):
    try:
        setattr(manufacturer, attribute_name, new_value)
        session.commit()
    except ValueError:
        print('Incorrect argument entered')
        session.rollback()
