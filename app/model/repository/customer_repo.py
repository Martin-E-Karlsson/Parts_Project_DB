from model.db import session
from model.models.customer import Customer


def insert_customer(address, id_contact):
    new_customer = Customer(
        Address=address,
        idContact=id_contact
    )
    session.add(new_customer)
    session.commit()


def get_all_customers():
    return session.query(Customer).all()


def get_customer_by_id(id_customer):
    return session.query(Customer).filter(Customer.idCustomer == id_customer).first()


def get_all_customers_by_attribute(attribute_name, value):
    try:
        return session.query(Customer).filter(getattr(Customer, attribute_name).like(f"%{value}%")).all()
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_customer_attribute(customer, attribute_name, new_value):
    try:
        setattr(customer, attribute_name, new_value)
        session.commit()
    except ValueError:
        print('Incorrect argument entered')
        session.rollback()
