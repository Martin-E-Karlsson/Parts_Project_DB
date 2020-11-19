import model.repository.retailer_repo as rr


def insert_retailer(name, address, id_contact=None, id_manufacturer=None):
    rr.insert_retailer(name, address, id_contact, id_manufacturer)


def get_all_retailers():
    return rr.get_all_retailers()


def get_retailer_by_id(id_retailer):
    return rr.get_retailer_by_id(id_retailer)


def get_retailer_by_name(name):
    retailers = rr.get_retailer_by_name(name)
    return {i+1: retailer for i, retailer in enumerate(retailers)}


def change_retailer_name(retailer, new_name):
    rr.change_retailer_name(retailer, new_name)
