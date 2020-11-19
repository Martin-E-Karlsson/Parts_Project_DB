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


def get_store_inventory_by_store_id(id_store):
    return session.query(StoreInventory).filter(StoreInventory.idStore == id_store).first()


def get_store_inventory_by_product_id(id_product):
    return session.query(StoreInventory).filter(StoreInventory.idProduct == id_product).first()


def change_store_inventory_store_id(store_inventory, new_store_id):
    try:
        store_inventory.idStore = new_store_id
        session.commit()
    except:
        session.rollback()


def change_store_inventory_product_id(store_inventory, new_product_id):
    try:
        store_inventory.idProduct = new_product_id
        session.commit()
    except:
        session.rollback()
