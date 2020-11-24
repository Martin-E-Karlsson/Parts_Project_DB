from controller.customer_controller import get_all_customers
from controller.customer_controller import insert_customer
from controller.customer_controller import get_customer_by_id
from controller.customer_controller import get_customer_by_address
from controller.customer_controller import change_customer_address
from controller.controller import store_changes


def customers_menu():
    while True:
        print("Customers menu")
        print("xxxxxxxx")
        print("1. Add a new customer")
        print("2. View all the customers")
        print("3. View customer by id")
        print("4. View/edit customer by address")
        print("5. Quit customers menu")
        selection = input("> ")
        if selection == "1":
            address = input("Specifiy the address of the customer: ")
            id_contact = input("Indicate the id_contact of the customer: ")
            insert_customer(address, id_contact)
        elif selection == "2":
            customers = get_all_customers()
            for customer in customers:
                print(customer)
        elif selection == "3":
            id = input("Indicate customer id: ")
            customer = get_customer_by_id(id)
            if customer:
                print(customer)
            else:
                print("Could not find a customer with id", id)
        elif selection == "4":
            address = input("Enter complete or partial address: ")
            customers= get_customer_by_address(address)
            for key, customer in customers.items():
                print(f"{key}.{customer}")
            edit_selection = input("Enter number for customer to edit: ")
            edit_selection = int(edit_selection)

            customer = customers[edit_selection]
            print(f" 1. Customer Address: {customer.Address}")
            new_value = input("Enter a new address: ")
            change_customer_address(customer, new_value)
        elif selection == "5":
            break

