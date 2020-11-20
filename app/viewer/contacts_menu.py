from controller.contacts_controller import view_all_contacts
from controller.contacts_controller import c.add_new_contacts()
from controller.companies_controller import add_new_company_address()
from .customers_menu import add_customers
from .companies_menu import add_new_company

def add_new_contacts():
    print("Is the contact a company?")
    answer = None
    while answer not in ("yes", "no"):
        answer = input("Write yes or no: ")
        if answer.lower() == "yes":
            add_new_company()       # Calls a method in companies_menu.py
            c.add_new_contacts()  # Calls a method to be created in controller
        elif answer.lower() == "no":
            c.add_new_contacts  # Calls a method to be created in controller
        else:
            print("Write yes or no: ")

def update_contact():
    print("Is the contact of a company?")
    answer = None
    while answer not in ("yes", "no"):
        answer = input("Write yes or no: ")
        if answer.lower() == "yes":
            print("Do you want to update the address?")
            answer1 = None
            while answer1 not in ("yes", "no"):
                answer1 = input("Write yes or no: ")
                if answer1.lower() == "yes":
                    add_new_company_address()  # Calls a method to be created in controller
                elif  answer1.lower() == "no":
                    c.update_contact()  # Calls a method to be created in controller
                else:
                    print("Write yes or no: ")
        elif answer.lower() == "no":
            c.update_contact()          # Calls a method to be created in controller
        else:
            print("Write yes or no: ")

def contacts_menu():
    while True:
        print("Contacts menu")
        print("xxxxxxxx")
        print("1. View all the contacts")
        print("2. Add contacts")
        print("3. Update information of a contact")
        print("4. Quit contacts menu")
        selection = input("> ")
                if selection == "1":
                    view_all_contacts()         # Calls to method in controller
                elif selection == "2":
                    print("Is the contact a company?")
                    answer = input("yes or no: ")
                    if answer.lower() == "no":
                        add_new_contacts()      # Calls to method in controller
                        add_customers()         #Calls to method in file customer_menu.py
                    elif answer.lower =="yes":
                        add_new_company()       #Calls to method in file companies_menu.py
                    else:
                        print("Write yer or no")
                elif selection == "3":
                    update_contact()
                elif selection =="4":
                    break
