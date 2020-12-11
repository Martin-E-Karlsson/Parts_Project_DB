from model.models.orders import Order


def insert_order(customer_id, product_id, order_date, product_quantity, employee_id):
    new_order = Order({'customer_id': customer_id,
                       'products': [{
                           'product_id': product_id,
                           'order_date': order_date,
                           'product_quantity': product_quantity,
                           'employee_id': employee_id}]}
    )
    new_order.save()


def get_all_orders():
    return Order.all()


def get_order_by_order_id(order_id):
    return Order.find(_id=order_id)


def change_order_attribute(order_id, attribute_name, new_value):
    try:
        Order.change_attribute(order_id, attribute_name, new_value)
    except ValueError:
        print('Incorrect argument entered')
