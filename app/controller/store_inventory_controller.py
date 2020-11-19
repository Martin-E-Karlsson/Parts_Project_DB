import model.repository.store_inventory_repo as sir


def insert_store_inventory(id_product, id_store):
    sir.insert_store_inventory(id_product, id_store)


def get_all_store_inventories():
    return sir.get_all_store_inventories()


def get_store_inventory_by_store_id(id_store):
    return sir.get_store_inventory_by_store_id(id_store)


def get_store_inventory_by_product_id(id_product):
    return sir.get_store_inventory_by_product_id(id_product)


def change_store_inventory_store_id(store_inventory, new_store_id):
    sir.change_store_inventory_store_id(store_inventory, new_store_id)


def change_store_inventory_product_id(store_inventory, new_product_id):
    sir.change_store_inventory_product_id(store_inventory, new_product_id)
