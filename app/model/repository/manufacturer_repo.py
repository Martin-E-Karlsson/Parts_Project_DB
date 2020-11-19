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


def get_manufacturer_by_name(manufacturer_name):
    return session.query(Manufacturer).filter(Manufacturer.ManufacturerName.like(f"%{manufacturer_name}%").all())


def change_manufacturer_name(manufacturer, new_manufacturer_name):
    try:
        manufacturer.ManufacturerName = new_manufacturer_name
        session.commit()
    except:
        session.rollback()