from model.db import session
from model.models.store_inventory import StoreInventory


def insert_store_inventory(id_product, id_store):
    new_store_inventory = StoreInventory(
        idProduct=id_product,
        idStore=id_store
    )
    session.add(new_store_inventory)
    session.commit()


def get_all_store_inventories():
    return session.query(StoreInventory).all()


def get_all_store_inventories_by_attribute(attribute_name, value):
    try:
        return session.query(StoreInventory).filter(getattr(StoreInventory, attribute_name).like(f"%{value}%")).all()
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_store_inventory_attribute(store_inventory, attribute_name, new_value):
    try:
        setattr(store_inventory, attribute_name, new_value)
        session.commit()
    except ValueError:
        print('Incorrect argument entered')
        session.rollback()
