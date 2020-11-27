from model.db import session
from model.models.order_details import OrderDetails


def insert_order_details(product_quantity, purchase_date, id_order, id_product, id_employee):
    new_order_details = OrderDetails(
        ProductQuantity=product_quantity,
        PurchaseDate=purchase_date,
        idOrder=id_order,
        idProduct=id_product,
        idEmployee=id_employee
    )
    session.add(new_order_details)
    session.commit()


def get_all_order_details():
    return session.query(OrderDetails).all()


def get_order_details_by_order_id(id_order):
    return session.query(OrderDetails).filter(OrderDetails.idOrder == id_order).first()


# TODO: Order details to be searchable by entering year/month/day. get_order_details_by_purchase_date(year, month, day)
def get_all_order_details_with_purchase_date(purchase_date):
    return session.query(OrderDetails).filter(OrderDetails.PurchaseDate == purchase_date).first()


def get_all_order_details_by_attribute(attribute_name, value):
    try:
        return session.query(OrderDetails).filter(getattr(OrderDetails, attribute_name).like(f"%{value}%")).all()
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_order_details_attribute(order_details, attribute_name, new_value):
    try:
        setattr(order_details, attribute_name, new_value)
        session.commit()
    except ValueError:
        print('Incorrect argument entered')
        session.rollback()
