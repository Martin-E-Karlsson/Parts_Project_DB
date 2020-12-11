import model.repository.customer_repo as cr


def insert_customer(name, phone_number, email, address, company_name=None):
    cr.insert_customer(name, phone_number, email, address, company_name)


def get_all_customers():
    return cr.get_all_customers()


def get_customer_by_id(customer_id):
    return cr.get_customer_by_id(customer_id)


def get_all_customers_by_attribute(attribute_name, value):
    customers = cr.get_all_customers_by_attribute(attribute_name, value)
    return {i+1: customer for i, customer in enumerate(customers)}


def change_customer_attribute(customer_id, attribute_name, new_value):
    cr.change_customer_attribute(customer_id, attribute_name, new_value)
