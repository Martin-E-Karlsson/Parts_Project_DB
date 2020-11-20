from controller.customer_controller import view_all_customers
from controller.customer_controller import add_customers
from controller.customer_controller import update_customer_address


from .contacts_menu import add_new_contacts
from .contacts_menu import update_contact

def customers_menu():
    while True:
        print("Customers menu")
        print("xxxxxxxx")
        print("1. View all the customers")
        print("2. Add a new customer")
        print("3. Update information of a customer")
        print("4. Quit customers menu")
        selection = input("> ")
                if selection == "1":
                    customers = view_all_customers()    #Calls a method to be created in controller
                    for customer in customers:
                        print(customer)
                elif selection == "2":
                    add_new_contacts()      #Calls a method in file contacts_menu.py
                    add_customers()         #Calls a method to be created in controller
                elif selection == "3":
                    print("Want to update address?")
                    answer = None
                    while answer not in ("yes", "no"):
                        answer = input("Write yes or no: ")
                        if answer.lower()== "yes":
                            update_customer_address()   #Calls a method to be created in controller
                        elif answer.lower() =="no":
                            update_contact()            # Calls a method in file contacts_menu.py
                        else:
                            print("Write yes or no: ")
                elif selection =="4":
                    break
