from controller.warehouse_controller import get_all_warehouses, get_warehouse_by_id, \
    get_warehouses_by_product_delivery_date, change_product_in_storage



def warehouse_menu():
    while True:
        print("warehouse_menu")
        print("xxxxxxxx")
        print("1. View all warehouses")
        print("2. View warehous by id")
        print("3. get warehouses by product delivery date")
        print("4. change product in storage")
        print("5. Quit customers menu")
        selection = input("> ")
        if selection == "1":
            warehouses = get_all_warehouses()
            for i in warehouses:
                print(i)
        elif selection == "2":
            print("input warehouse id")
            id_warehouse = input("> ")
            print(get_warehouse_by_id(int(id_warehouse)))

        elif selection == "3":
            print("input date")
            year = input("yyyy > ")
            month = input("mm > ")
            day = input("dd > ")
            product_delivery_date = f"{year}-{month}-{day}"
            print(get_warehouses_by_product_delivery_date(product_delivery_date))

        elif selection == "4":
            print("witch warehouse?")
            warehouse = input("> ")
            print("how many items is in storge?")
            new_product_in_storage = input("> ")
            change_product_in_storage(int(warehouse), int(new_product_in_storage))

        elif selection == "5":
            break
        print()
