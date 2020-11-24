from controller.manufacturer_controller import insert_manufacturer, get_all_manufacturers, get_manufacturer_by_id, \
    get_manufacturer_by_name, change_manufacturer_name


def manufacturers_menu():
    while True:
        print("Manufacturers menu")
        print("xxxxxxxx")
        print("1. Add a new manufacturer")
        print("2. View all the manufacturers")
        print("3. View manufacturer by id")
        print("4. View/edit manufacturer by name")
        print("5. Quit manufacturers menu")
        selection = input("> ")
        if selection == "1":
            hq_address = input("Indicate the address of the manufacturer: ")
            hq_phone_number = input("Indicate the phone number of the manufacturer: ")
            manufacturer_name = input("Indicate the name of the manufacturer: ")
            insert_manufacturer(hq_address, hq_phone_number, manufacturer_name)
        elif selection == "2":
            manufacturers = get_all_manufacturers()
            for manufacturer in manufacturers:
                print(manufacturer)
        elif selection == "3":
            id_manufacturer = input("Indicate manufacturer's id: ")
            manufacturer = get_manufacturer_by_id(id_manufacturer)
            if manufacturer:
                print(manufacturer)
            else:
                print("Could not find a manufacturer with id", id_manufacturer)
        elif selection == "4":
            manufacturer_name = input("Enter complete or partial manufacturer's name: ")
            manufacturers= get_manufacturer_by_name(manufacturer_name)
            for key, manufacturer in manufacturers.items():
                print(f"{key}.{manufacturer}")
            edit_selection = input("Enter number for manufacturer to edit: ")
            edit_selection = int(edit_selection)

            manufacturer = manufacturers[edit_selection]
            print(f" 1. Manufacturer name: {manufacturer.ManufacturerName}")
            new_manufacturer_name = input("Enter a new manufacturer's name: ")
            change_manufacturer_name(manufacturer, new_manufacturer_name)
        elif selection == "5":
            break