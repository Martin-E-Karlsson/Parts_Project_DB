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
        print("1. Customers")
        print("2. Cars")
        print("3. Manufacturer")
        print("4. Products")
        print("5. Retailer")
        print("6. Stores")
        print("7. Employees")

        selection = input("> ")
        if selection == "1":
            customers_menu()
        elif selection == "2":
            cars_menu()
        elif selection == "3":
            manufacturers_menu()
        elif selection == "4":
            products_menu()
        elif selection == "5":
            retailers_menu()
        elif selection == "6":
            store_menu()
        elif selection == "7":
            emloyees_menu()
        else:
            break
