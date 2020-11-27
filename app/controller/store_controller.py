import model.repository.store_repo as sr


def insert_store(name, store_type):
    sr.insert_store(name, store_type)


def get_all_stores():
    return sr.get_all_stores()


def get_store_by_id(id_store):
    return sr.get_store_by_id(id_store)


def get_all_stores_by_attribute(attribute_name, value):
    stores = sr.get_all_stores_by_attribute(attribute_name, value)
    return {i+1: store for i, store in enumerate(stores)}


def change_store_attribute(store, attribute_name, new_value):
    sr.change_store_attribute(store, attribute_name, new_value)
