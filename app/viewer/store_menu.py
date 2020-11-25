from controller.store_controller import insert_store, get_all_stores, get_store_by_id, get_stores_by_name, \
    get_stores_by_type, change_store_name, change_store_type


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
            s = get_stores_by_name(name)
            [print(k, " : ", s[k]) for k in s]
        elif selection == "5":
            print("Type of store")
            store_type = input("> ")
            s = get_stores_by_type(store_type)
            [print(k, ":", s[k]) for k in s]
        elif selection == "6":
            print("which do you want to rename (id)")
            id_store = input("> ")
            store = get_store_by_id(int(id_store))
            print("New name of store")
            new_name = input("> ")
            change_store_name(store, new_name)
        elif selection == "7":
            print("which store do you want to change (id)")
            id_store = input("> ")
            store = get_store_by_id(int(id_store))
            print(f"{store.Name} was a {store.StoreType}")
            if store.StoreType == "online butik":
                change_store_type(store, "fysisk butik")
            else:
                change_store_type(store, "online butik")
            print(f"{store.Name} is now a {store.StoreType}")
        elif selection == "8":
            break
        print()
store_menu()
