import model.repository.order_repo as orp


def insert_order(id_customer):
    orp.insert_car(id_customer)


def get_all_orders():
    return orp.get_all_orders()


def get_order_by_order_id(id_order):
    return orp.get_order_by_order_id(id_order)
