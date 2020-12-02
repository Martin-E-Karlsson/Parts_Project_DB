from . import session
from model.models.mysql_db import Manufacturer
import model.models.manufacturers as ma


def fix_manufacturers():
    manufacturers = session.query(Manufacturer).all()
    for manufacturer in manufacturers:
        as_dict = manufacturer.__dict__
        as_dict['_id'] = int(as_dict['idManufacturer'])
        as_dict['hq_address'] = str(as_dict['HQAdress'])
        as_dict['hq_phone_number'] = str(as_dict['HQPhoneNumber'])
        as_dict['name'] = str(as_dict['ManufacturerName'])
        del as_dict['_sa_instance_state']
        del as_dict['idManufacturer']
        del as_dict['HQAdress']
        del as_dict['HQPhoneNumber']

        mongo_manufacturer = ma.Manufacturer(as_dict)
        mongo_manufacturer.insert()
