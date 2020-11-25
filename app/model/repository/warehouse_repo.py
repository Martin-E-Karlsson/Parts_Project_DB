from model.db import session
from model.models.warehouse import Warehouse


def insert_warehouse(product_in_storage, minimal_amount_in_storage, amount_to_be_delivered, product_delivery_date):
    new_warehouse = Warehouse(
        ProductInStorage=product_in_storage,
        MinimalAmountInStorage=minimal_amount_in_storage,
        AmountToBeDelivered=amount_to_be_delivered,
        ProductDeliveryDate=product_delivery_date
    )
    session.add(new_warehouse)
    session.commit()


def get_all_warehouses():
    return session.query(Warehouse).all()


def get_warehouse_by_id(id_warehouse):
    return session.query(Warehouse).filter(Warehouse.idWarehouse == id_warehouse).first()


def get_all_warehouses_with_product_delivery_date(product_delivery_date):
    return session.query(Warehouse).filter(Warehouse.ProductDeliveryDate == product_delivery_date).all()


def change_product_in_storage(warehouse, new_product_in_storage):
    try:
        warehouse.ProductInStorage = new_product_in_storage
        session.commit()
    except:
        session.rollback()