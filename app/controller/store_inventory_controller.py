import model.repository.store_inventory_repo as sir


def insert_store_inventory(id_product, id_store):
    sir.insert_store_inventory(id_product, id_store)


def get_all_store_inventories():
    return sir.get_all_store_inventories()


def get_all_store_inventories_by_attribute(attribute_name, value):
    store_inventories = sir.get_all_store_inventories_by_attribute(attribute_name, value)
    return {i+1: store_inventory for i, store_inventory in enumerate(store_inventories)}


def change_store_inventory_attribute(store_inventory, attribute_name, new_value):
    sir.change_store_inventory_attribute(store_inventory, attribute_name, new_value)
