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


def get_order_details_by_purchase_date(purchase_date):
    return session.query(OrderDetails).filter(OrderDetails.PurchaseDate == purchase_date).first()


def change_order_details_product_quantity(order_details, new_product_quantity):
    try:
        order_details.ProductQuantity = new_product_quantity
        session.commit()
    except:
        session.rollback()