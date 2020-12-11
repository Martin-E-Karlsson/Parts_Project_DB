from controller.product_controller import insert_product, get_all_products, get_product_by_id,\
    get_all_products_by_attribute, change_product_attribute


def products_menu():
    while True:
        print("Poducts menu")
        print("xxxxxxxx")
        print("1. Add a new product")
        print("2. View all the products")
        print("3. View product by id")
        print("4. View/edit product by name")
        print("5. Quit products menu")
        selection = input("> ")
        if selection == "1":
            name = input("Write the product name: ")
            retailer = input("Write the product retailer: ")
            description = input("Write the product description: ")
            purchase_cost = input("Write the product purchase_cost: ")
            sell_price = input("Write the product sell_price: ")
            id_source = input("Write the product id_source: ")
            id_warehouse = input("Write the product id_warehouse: ")
            insert_product(name, retailer, description, purchase_cost, sell_price, id_source, id_warehouse)
        elif selection == "2":
            products = get_all_products()
            for product in products:
                print(product)
        elif selection == "3":
            id_product = input("Indicate product id: ")
            product = get_product_by_id(id_product)
            if product:
                print(product)
            else:
                print("Could not find a product with product id ", id_product)
        elif selection == "4":
            name = input("Enter complete or partial name: ")
            products = get_all_products_by_attribute(name)
            for key, product in products.items():
                print(f"{key}.{product}")
            edit_selection = input("Enter product number and edit name: ")
            edit_selection = int(edit_selection)

            product = products[edit_selection]
            print(f" 1. Product name: {product.Name}")
            new_name = input("Enter a new product name: ")
            change_product_attribute(product, new_name)
        elif selection == "5":
            break