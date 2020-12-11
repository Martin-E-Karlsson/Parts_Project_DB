from model.models.stores import Store


def insert_store(name, store_type):
    new_store = Store({'name': name,
                       'store_type': store_type,
                       'employees': [],
                       'product_id': []})
    new_store.save()


def get_all_stores():
    return Store.all()


def get_store_by_id(store_id):
    return Store.find(_id=store_id)


def get_all_stores_by_attribute(attribute_name, value):
    try:
        return Store.find(**{attribute_name: value})
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_store_attribute(store_id, attribute_name, new_value):
    try:
        Store.change_attribute(store_id, attribute_name, new_value)
    except ValueError:
        print('Incorrect argument entered')

