import model.repository.order_details_repo as odr


def insert_order_details(product_quantity, purchase_date, id_order, id_product, id_employee):
    odr.insert_order_details(product_quantity, purchase_date, id_order, id_product, id_employee)


def get_all_order_details():
    return odr.get_all_order_details()


def get_order_details_by_order_id(id_order):
    return odr.get_order_details_by_order_id(id_order)


# TODO: Order details to be searchable by entering year/month/day. get_order_details_by_purchase_date(year, month, day)
def get_all_order_details_with_purchase_date(purchase_date):
    order_details = odr.get_all_order_details_with_purchase_date(purchase_date)
    return {i+1: order_detail for i, order_detail in enumerate(order_details)}


def change_order_details_product_quantity(order_details, new_product_quantity):
    odr.change_order_details_product_quantity(order_details, new_product_quantity)
