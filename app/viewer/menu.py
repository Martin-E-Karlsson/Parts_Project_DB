from viewer.customers_menu import customers_menu
from viewer.contacts_menu import contacts_menu
from viewer.orders_details_menu import order_details_menu
from viewer.companies_menu import companies_menu


def main_menu():
    while True:
        print("Main menu")
        print("========")
        print("1. Customers")
        print("2. Contacts ")
        print("3. Companies")
        print("4. Orders details")

        selection = input("> ")
        if selection == "1":
            customers_menu()
        elif selection == "2":
            contacts_menu()
        elif selection == "3":
            companies_menu()
        elif selection == "4":
            order_details_menu()
        else:
            break

