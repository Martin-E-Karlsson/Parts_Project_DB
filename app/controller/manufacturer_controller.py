import model.repository.manufacturer_repo as mr


def insert_manufacturer(hq_address, hq_phone_number, manufacturer_name):
    mr.insert_manufacturer(hq_address, hq_phone_number, manufacturer_name)


def get_all_manufacturers():
    return mr.get_all_manufacturers()


def get_manufacturer_by_id(id_manufacturer):
    return mr.get_manufacturer_by_id(id_manufacturer)


def get_all_manufacturers_with_name(manufacturer_name):
    manufacturers = mr.get_all_manufacturers_with_name(manufacturer_name)
    return {i+1: manufacturer for i, manufacturer in enumerate(manufacturers)}


def change_manufacturer_name(manufacturer, new_manufacturer_name):
    mr.change_manufacturer_name(manufacturer, new_manufacturer_name)
