from model.db import session
from model.models.order import Order


def insert_order(id_customer):
    new_order = Order(idCustomer=id_customer)
    session.add(new_order)
    session.commit()


def get_all_orders():
    return session.query(Order).all()


def get_order_by_order_id(id_order):
    return session.query(Order).filter(Order.idOrder == id_order).first()
