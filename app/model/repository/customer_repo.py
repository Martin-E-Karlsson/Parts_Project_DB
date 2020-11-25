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


def get_customer_by_contact_id(id_contact):
    return session.query(Customer).filter(Customer.idContact == id_contact).first()


def get_all_customers_with_address(address):
    return session.query(Customer).filter(Customer.Address.like(f"%{address}%").all())


def change_customer_address(customer, new_address):
    try:
        customer.Address = new_address
        session.commit()
    except:
        session.rollback()