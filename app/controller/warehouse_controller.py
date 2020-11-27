import model.repository.warehouse_repo as wr


def insert_warehouse(product_in_storage, minimal_amount_in_storage, amount_to_be_delivered, product_delivery_date):
    wr.insert_warehouse(product_in_storage, minimal_amount_in_storage, amount_to_be_delivered, product_delivery_date)


def get_all_warehouses():
    return wr.get_all_warehouses()


def get_warehouse_by_id(id_warehouse):
    return wr.get_warehouse_by_id(id_warehouse)


def get_all_warehouses_by_attribute(attribute_name, value):
    warehouses = wr.get_all_warehouses_by_attribute(attribute_name, value)
    return {i+1: warehouse for i, warehouse in enumerate(warehouses)}


def change_warehouse_attribute(warehouse, attribute_name, new_value):
    wr.change_warehouse_attribute(warehouse, attribute_name, new_value)
