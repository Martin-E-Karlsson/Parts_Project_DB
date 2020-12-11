from model.models.orders import Order


def insert_order(customer_id,product_id,order_date,product_quantity,employee_id):

    new_order = Order({'customer_id': customer_id,
                       'products': [{
                           'product_id':product_id,
                           'order_date':order_date,
                           'product_quantity':product_quantity,
                           'employee_id':employee_id}]}
    )
    Order.save()



def get_all_orders():
    return Order.all()


def get_order_by_order_id(id_order):
    return Order.find(_id=id_order)


def change_customer_id(order, new_value):
    try:
        Order.change_attribute(order, 'customer_id', new_value)
    except ValueError:
        print('Incorrect argument entered')
