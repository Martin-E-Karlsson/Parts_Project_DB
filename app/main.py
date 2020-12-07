from model.db import Base, session
from model.db.fixes import *
from model.models.customers import Customer


def main():
    # print(Customer.find())
    # print(type(Customer.find()))
    # print(Customer.find(name='Henrik'))
    # print(Customer.find(_id=1, name='Martin'))
    customer = Customer.find(_id=1, name='Martin')
    print(customer)
    customer[0].phone_number = "777-777-777"
    print(customer)
    customer_as_dict = customer[0].__dict__
    Customer.replace_document(customer_as_dict['_id'], customer_as_dict)



if __name__ == '__main__':
    main()
