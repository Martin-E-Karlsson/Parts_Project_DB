import model.repository.order_repo as orp


def insert_order(customer_id, product_id, order_date, product_quantity, employee_id):
    orp.insert_car(customer_id, product_id, order_date, product_quantity, employee_id)


def get_all_orders():
    return orp.get_all_orders()


def get_order_by_order_id(order_id):
    return orp.get_order_by_order_id(order_id)


def change_order_attribute(order_id, attribute_name, new_value):
    orp.change_order_attribute(order_id, attribute_name, new_value)