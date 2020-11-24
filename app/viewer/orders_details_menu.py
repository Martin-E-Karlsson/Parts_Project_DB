from datetime import datetime

from controller.order_controller import insert_order
from controller.order_details_controller import insert_order_details, get_all_order_details, \
    get_order_details_by_order_id, get_order_details_by_purchase_date, change_order_details_product_quantity
from controller.product_controller import get_product_by_name


def orders_details_menu():
    while True:
        print("Orders details menu")
        print("xxxxxxxx")
        print("1. Add an order details")
        print("2. View all the orders details")
        print("3. View/edit order detail by order id")
        print("4. View order details by purchase date")
        print("5. Quit orders details menu")
        selection = input("> ")
        if selection == "1":
            id_customer = input("Write the id of the customer: ")
            add_order = insert_order(id_customer)
            id_order = add_order.idOrder
            name = input("Write the complete or partial name of the product: ")
            products = get_product_by_name(name)
            for key, product in products.items():
                print(f"{key}.{product}")
            select_product = input("Enter the number of the product to be selected: ")
            select_product = int(select_product)
            product = products[select_product]
            id_product = product.idProduct
            id_employee = input("Write your employee id: ")
            product_quantity = input("Write the number of products: ")
            purchase_date = datetime.now
            insert_order_details(product_quantity, purchase_date, id_order, id_product, id_employee)
        elif selection == "2":
            orders_details = get_all_order_details()
            for order_details in orders_details:
                print(order_details)
        elif selection == "3":
            id_order = input("Indicate order id: ")
            order_details = get_order_details_by_order_id(id_order)
            if order_details:
                print(order_details)
                print("Want to edit product quantities in order details?")
                print("Write yes or no: ")
                answer = None
                while answer not in ("yes", "no"):
                    answer = input("Enter yes or no: ")
                    if answer.lower() == "yes":
                        new_product_quantity = input("Indicate a new product quantity: ")
                        change_order_details_product_quantity(order_details,new_product_quantity)
                    elif answer.lower() == "no":
                        break
                    else:
                        print("Please write yes or no.")
            else:
                print("Could not find an order details with order id", id_order)
        elif selection == "4":
            purchase_date_day = input("Indicate purchase date day: ")
            purchase_date_month = input("Indicate purchase date month: ")
            purchase_date_year = input("Indicate purchase date year(4 digits): ")
            order_details_by_purchase_date = get_order_details_by_purchase_date(purchase_date_year, purchase_date_month, purchase_date_day)
            if order_details_by_purchase_date:
                print(order_details_by_purchase_date)
            else:
                print("Could not find an order details associate to the purchase date: ", purchase_date_year,"-",purchase_date_month,"-",purchase_date_day)
        elif selection == "5":
            break

