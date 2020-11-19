import model.repository.warehouse_repo as wr


def insert_warehouse(product_in_storage, minimal_amount_in_storage, amount_to_be_delivered, product_delivery_date):
    wr.insert_warehouse(product_in_storage, minimal_amount_in_storage, amount_to_be_delivered, product_delivery_date)


def get_all_warehouses():
    return wr.get_all_warehouses()


def get_warehouse_by_id(id_warehouse):
    return wr.get_warehouse_by_id(id_warehouse)


def get_warehouses_by_product_delivery_date(product_delivery_date):
    warehouses = wr.get_warehouses_by_product_delivery_date(product_delivery_date)
    return {i+1: warehouse for i, warehouse in enumerate(warehouses)}


def change_product_in_storage(warehouse, new_product_in_storage):
    wr.change_product_in_storage(warehouse, new_product_in_storage)
