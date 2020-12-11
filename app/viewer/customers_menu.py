
from controller.customer_controller import get_all_customers, insert_customer, get_customer_by_id, get_all_customers_by_attribute



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
            print("Please enter the required information below: ")
            name = input("Customer name:\n>")
            phone_number = input("Customer phone number:\n>")
            email = input("Customer email:\n>")
            address = input("Customer address:\n>")
            company_answer = input("Does this customer represent a company? (y/n)")
            if company_answer.lower() in ["y, yes", "yeah", "yarr", "ja", "ye"]:
                company_name = input("Please enter the name of the company:\n>")
            else:
                company_name = None
            insert_customer(name, phone_number, email, address, company_name)
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
            customers = get_all_customers_by_attribute(address)
            for key, customer in customers.items():
                print(f"{key}.{customer}")
            edit_selection = input("Enter number for customer to edit: ")
            edit_selection = int(edit_selection)

            customer = customers[edit_selection]
            print(f" 1. Customer Address: {customer.Address}")
            new_value = input("Enter a new address: ")
            get_all_customers_by_attribute(customer, new_value)
        elif selection == "5":
            break

