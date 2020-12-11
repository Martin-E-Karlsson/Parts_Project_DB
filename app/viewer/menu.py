from viewer.cars_menu import cars_menu
from viewer.customers_menu import customers_menu
from viewer.manufacturers_menu import manufacturers_menu
from viewer.employees_menu import emloyees_menu
from viewer.products_menu import products_menu
from viewer.retailers_menu import retailers_menu
from viewer.store_menu import store_menu


def main_menu():
    while True:
        print("Main menu")
        print("========")
        print("1. Cars")
        print("2. Customers")
        print("3. Employees")
        print("4. Manufacturer")
        print("5. Products")
        print("6. Retailer")
        print("7. Stores")

        selection = input("> ")
        if selection == "1":
            cars_menu()
        elif selection == "2":
            customers_menu()
        elif selection == "3":
            emloyees_menu()
        elif selection == "4":
            manufacturers_menu()
        elif selection == "5":
            products_menu()
        elif selection == "6":
            retailers_menu()
        elif selection == "7":
            store_menu()
        else:
            break
