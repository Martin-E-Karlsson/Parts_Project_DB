from model.models.customers import Customer


def insert_customer(name, phone_number, email, address, company_name=None):
    new_customer = Customer(
        {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'address': address,
            'cars': [],
            'orders': [],
            'company_name': company_name
        }
    )
    new_customer.save()


def get_all_customers():
    return Customer.all()


def get_customer_by_id(id_customer):
    return Customer.find(_id=id_customer)


def get_all_customers_by_attribute(attribute_name, value):
    try:
        return Customer.find(**{attribute_name: value})
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_customer_attribute(customer_id, attribute_name, new_value):
    try:
        Customer.change_attribute(customer_id, attribute_name, new_value)
    except ValueError:
        print('Incorrect argument entered')
