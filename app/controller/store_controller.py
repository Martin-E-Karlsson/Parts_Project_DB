import model.repository.store_repo as sr


def insert_store(name, store_type):
    sr.insert_store(name, store_type)


def get_all_stores():
    return sr.get_all_stores()


def get_store_by_id(id_store):
    return sr.get_store_by_id(id_store)


def get_stores_by_name(name):
    stores = sr.get_stores_by_name(name)
    return {i+1: store for i, store in enumerate(stores)}


def get_stores_by_type(store_type):
    stores = sr.get_stores_by_type(store_type)
    return {i+1: store for i, store in enumerate(stores)}


def change_store_name(store, new_name):
    sr.change_store_name(store, new_name)


def change_store_type(store, new_type):
    sr.change_store_type(store, new_type)
