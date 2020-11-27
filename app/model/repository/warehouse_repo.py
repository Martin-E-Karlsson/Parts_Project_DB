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


def get_all_warehouses_by_attribute(attribute_name, value):
    try:
        return session.query(Warehouse).filter(getattr(Warehouse, attribute_name).like(f"%{value}%")).all()
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_warehouse_attribute(warehouse, attribute_name, new_value):
    try:
        setattr(warehouse, attribute_name, new_value)
        session.commit()
    except ValueError:
        print('Incorrect argument entered')
        session.rollback()
