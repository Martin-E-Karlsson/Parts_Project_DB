from controller.store_inventory_controller import insert_store_inventory, get_all_store_inventories, \
    get_store_inventory_by_store_id, get_store_inventory_by_product_id, change_store_inventory_store_id, \
    change_store_inventory_product_id


def store_inventory_menu():
    while True:
        print("store inventory menu")
        print("xxxxxxxx")
        print("1. Add new item to store")
        print("2. View all store inventory ids")
        print("3. View stores")
        print("4. see product in storage")
        print("5. Quit customers menu")
        selection = input("> ")

        if selection == "1":
            print("input store id")
            id_store = input("> ")
            print("input product id")
            id_product = input("> ")

            insert_store_inventory(id_product, id_store)
        elif selection == "2":
            store_inventories = get_all_store_inventories()
            [print(i) for i in store_inventories]

        elif selection == "3":
            print("input store id")
            id_store = input("> ")
            [print(i) for i in get_store_inventory_by_store_id(id_store)]

        elif selection == "4":
            print("input product id")
            id_product = input("> ")
            [print(i) for i in get_store_inventory_by_product_id(id_product)]

        elif selection == "5":
            break
        print()
