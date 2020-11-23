from controller.contact_controller import insert_contact, get_all_contacts, get_contact_by_id, get_contact_by_name
from controller.controller import store_changes

def contacts_menu():
    while True:
        print("Contacts menu")
        print("xxxxxxxx")
        print("1. Add a new contact")
        print("2. View all the contacts")
        print("3. View contact by id")
        print("4. View/edit contact name")
        print("5. Quit contacts menu")
        selection = input("> ")
                if selection == "1":
                    insert_contact()
                elif selection == "2":
                    contacts = get_all_contacts()
                    for contact in contacts:
                        print(contact)
                elif selection == "3":
                    id = input("Indicate contact id: ")
                    contact = get_contact_by_id(id)
                    if contact:
                        print(contact)
                    else:
                        print("Could not find a contact with id", id)
                elif selection == "4":
                    name = input("Enter complete or partial name: ")
                    customers = get_contact_by_name(name)
                    for key, customer in customers.items():
                        print(f"{key}.{customer}")
                    edit_selection = input("Enter number for contact to edit: ")
                    edit_selection = int(edit_selection)

                    customer = customers[edit_selection]
                    print(f" 1. Contact name: {customer.Name}")
                    customer.Name = input("Enter a new name: ")
                    store_changes()
                elif selection =="5":
                    break
