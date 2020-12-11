from model.models.manufacturers import Manufacturer


def insert_manufacturer(hq_address, hq_phone_number, manufacturer_name, name):
    new_manufacturer = Manufacturer({
        'hq_address': hq_address,
        'hq_phone_number': hq_phone_number,
        'ManufacturerName': manufacturer_name,
        'name': name}
    )
    new_manufacturer.save()


def get_all_manufacturers():
    return Manufacturer.all()


def get_manufacturer_by_id(id_manufacturer):
    return Manufacturer.find(_id=id_manufacturer)


def get_all_manufacturers_by_attribute(attribute_name, value):
    try:
        return Manufacturer.find(**{attribute_name: value})
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_store_attribute(store_id, attribute_name, new_value):
    try:
        Manufacturer.change_attribute(store_id, attribute_name, new_value)
    except ValueError:
        print('Incorrect argument entered')
