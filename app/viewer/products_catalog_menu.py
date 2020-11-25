from controller.product_catalog_controller import insert_product_catalog, get_all_product_catalogs, \
    get_product_catalog_by_product_id, get_product_catalogs_by_retailer_id


def products_catalog_menu():
    while True:
        print("Products catalog menu")
        print("xxxxxxxx")
        print("1. Add a new product catalog")
        print("2. View all the product catalogs")
        print("3. View product catalog by product id")
        print("4. View product catalog by retailer id")
        print("5. Quit products catalog menu")
        selection = input("> ")
        if selection == "1":
            id_product = input("Indicate the product id of the product catalog: ")
            id_retailer = input("Indicate the retailer id of the product catalog:: ")
            insert_product_catalog(id_product, id_retailer)
        elif selection == "2":
            product_catalogs = get_all_product_catalogs()
            for product_catalog in product_catalogs:
                print(product_catalog)
        elif selection == "3":
            id_product = input("Indicate the product id of the product catalog: ")
            product_catalog = get_product_catalog_by_product_id(id_product)
            if product_catalog:
                print(product_catalog)
            else:
                print("Could not find a product catalog with product id", id_product)
        elif selection == "4":
            id_retailer = input("Indicate the retailer id of the product catalog: ")
            product_catalog = get_product_catalogs_by_retailer_id(id_retailer)
            if product_catalog:
                print(product_catalog)
            else:
                print("Could not find a product catalog with retailer id", id_retailer)
        elif selection == "5":
            break