import model.repository.customer_repo as cr


def insert_customer(address, id_contact):
    cr.insert_customer(address, id_contact)


def get_all_customers():
    return cr.get_all_customers()


def get_customer_by_id(id_customer):
    return cr.get_customer_by_id(id_customer)


def get_all_customers_by_attribute(attribute_name, value):
    customers = cr.get_all_customers_by_attribute(attribute_name, value)
    return {i+1: customer for i, customer in enumerate(customers)}


def change_customer_attribute(customer, attribute_name, new_value):
    cr.change_customer_attribute(customer, attribute_name, new_value)
