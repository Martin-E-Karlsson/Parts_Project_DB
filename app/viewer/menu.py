from viewer import products_catalog_menu
from viewer.cars_menu import cars_menu
from viewer.customers_menu import customers_menu
from viewer.contacts_menu import contacts_menu
from viewer.manufacturers_menu import manufacturers_menu
from viewer.orders_details_menu import orders_details_menu
from viewer.companies_menu import companies_menu

from viewer.employees_menu import emloyees_menu
from viewer.products_menu import products_menu
from viewer.retailers_menu import retailers_menu
from viewer.source_menu import source_menu
from viewer.store_menu import store_menu
from viewer.store_inventory_menu import store_inventory_menu
from viewer.warehouse_menu import warehouse_menu


def main_menu():
    while True:
        print("Main menu")
        print("========")
        print("1. Customers")
        print("2. Contacts ")
        print("3. Companies")
        print("4. Orders details")
        print("5. Cars")
        print("6. Manufacturer")
        print("7. Orders")
        print("8. Products")
        print("9. Products catalog")
        print("10. Retailer")
        print("11. Sources")
        print("12. Stores")
        print("13. Store inventory")
        print("14. Warehouse")
        print("15. Employees")

        selection = input("> ")
        if selection == "1":
            customers_menu()
        elif selection == "2":
            contacts_menu()
        elif selection == "3":
            companies_menu()
        elif selection == "4":
            orders_details_menu()
        elif selection == "5":
            cars_menu()
        elif selection == "6":
            manufacturers_menu()
        elif selection == "7":
            pass
        elif selection == "8":
            products_menu()
        elif selection == "9":
            products_catalog_menu()
        elif selection == "10":
            retailers_menu()
        elif selection == "11":
            source_menu()
        elif selection == "12":
            store_menu()
        elif selection == "13":
            store_inventory_menu()
        elif selection == "14":
            warehouse_menu()
        elif selection == "15":
            emloyees_menu()
        else:
            break
