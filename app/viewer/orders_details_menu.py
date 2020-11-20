from controller.customer_controller import get_all_customers

def order_details_menu():
    while True:
        print("Customers menu")
        print("xxxxxxxx")
        print("1. View all the customers")
        print("2. Add a new customer")
        print("3. Update information of a customer")
        print("4. Quit customers menu")
        selection = input("> ")
                if selection == "1":
                    get_all_customers()
                elif selection == "2":
                    add_new_customer()
                elif selection == "3":
                    update_customer()
                elif selection =="4":
                    break

