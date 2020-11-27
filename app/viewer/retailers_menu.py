from controller.retailer_controller import insert_retailer, get_all_retailers, get_retailer_by_id, change_retailer_name, \
    get_all_retailers_with_name


def retailers_menu():
    while True:
        print("Retailers menu")
        print("xxxxxxxx")
        print("1. Add a new retailer")
        print("2. View all the retailers")
        print("3. View retailer by id")
        print("4. View/edit retailer by name")
        print("5. Quit retailers menu")
        selection = input("> ")
        if selection == "1":
            name = input("Indicate the name of the retailer: ")
            address = input("Indicate the address of the retailer: ")
            id_contact = input("Indicate the address of the retailer: ")
            id_manufacturer = input("Indicate the address of the retailer: ")
            insert_retailer(name, address, id_contact=None, id_manufacturer=None)
        elif selection == "2":
            retailers = get_all_retailers()
            for retailer in retailers:
                print(retailer)
        elif selection == "3":
            id_retailer = input("Indicate retailer id: ")
            retailer = get_retailer_by_id(id_retailer)
            if retailer:
                print(retailer)
            else:
                print("Could not find a retailer with id", id_retailer)
        elif selection == "4":
            name = input("Enter complete or partial name of the retailer: ")
            retailers= get_all_retailers_with_name(name)
            for key, retailer in retailers.items():
                print(f"{key}.{retailer}")
            edit_selection = input("Enter number for retailer to edit: ")
            edit_selection = int(edit_selection)

            retailer = retailers[edit_selection]
            print(f" 1. Retailer name: {retailer.Name}")
            new_name = input("Enter a new retailer name: ")
            change_retailer_name(retailer, new_name)
        elif selection == "5":
            break