from controller.source_controller import insert_source, get_all_sources, get_source_by_manufacturer_id, \
    change_source_manufacturer_id


def source_menu():
    while True:
        print("source_menu")
        print("xxxxxxxx")
        print("1. insert source")
        print("2. Show all source")
        print("3. Get source by manufacturer id")
        print("4. Change source manufacturer id")
        print("5. Quit source menu")
        selection = input("> ")
        if selection == "1":
            print("Input manufacturer id")
            manufacturer_id = input("> ")
            insert_source(manufacturer_id)
        if selection == "2":
            print(get_all_sources())
        if selection == "3":
            print("Input manufacturer id")
            manufacturer_id = input("> ")
            get_source_by_manufacturer_id(manufacturer_id)
        if selection == "4":
            print("which manufacturer id do you want to change")
            manufacturer_id = input("> ")
            source = get_source_by_manufacturer_id(manufacturer_id)
            print("what is the new id?")
            new_manufacturer_id = input("> ")
            change_source_manufacturer_id(source, new_manufacturer_id)
        if selection == "5":
            break
