from controller.store_controller import insert_store, get_all_stores, get_store_by_id, get_all_stores_by_attribute, \
    change_store_attribute


def store_menu():
    while True:
        print("store_menu")
        print("xxxxxxxx")
        print("1. Add new store")
        print("2. Show all stors")
        print("3. Show store by id")
        print("4. Show store by name")
        print("5. Show store by type")
        print("6. Change store name")
        print("7. Change store type")
        print("8. Quit store menu")
        selection = input("> ")

        if selection == "1":
            print("Name of new store")
            name = input("> ")
            print("is it a online store or a physical store?")
            store_type = input("> ")
            insert_store(name, store_type)

        elif selection == "2":
            [print(s) for s in get_all_stores()]

        elif selection == "3":
            print("input store ID")
            id_store = input("> ")
            print(get_store_by_id(int(id_store)))

        elif selection == "4":
            print("Name of store")
            name = input("> ")
            s = get_all_stores_by_attribute('name',name)
            [print(k, " : ", s[k]) for k in s]
        elif selection == "5":
            print("Type of store")
            store_type = input("> ")
            s = get_all_stores_by_attribute('store_type',store_type)
            [print(k, ":", s[k]) for k in s]

        elif selection == "6":
            print("which do you want to rename (id)")
            id_store = input("> ")
            store = get_store_by_id(int(id_store))
            print("New name of store")
            new_name = input("> ")
            change_store_attribute(store[0]._id,'name', new_name)
        elif selection == "7":
            print("which store do you want to change (id)")
            id_store = input("> ")
            store = get_store_by_id(int(id_store))
            print(f"{store[0].name} was a {store[0].store_type}")
            if store[0].store_type == "online butik":
                change_store_attribute(store[0]._id,'store_type', "fysisk butik")
            else:
                change_store_attribute(store[0]._id,'store_type', "online butik")
            print(f"{get_store_by_id(int(id_store))[0].name} is now a {get_store_by_id(int(id_store))[0].store_type}")
        elif selection == "8":
            break
        print()
