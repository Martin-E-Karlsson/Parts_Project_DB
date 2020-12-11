from controller.customer_controller import get_all_customers, insert_customer, get_all_customers_by_attribute, change_customer_attribute

POSITIVE_ANSWERS = ["y", "yes", "yeah", "yarr", "ja", "ye"]


def customers_menu():
    while True:
        print("Customers menu")
        print("xxxxxxxx")
        print("1. Add a new customer")
        print("2. View all the customers")
        print("3. View all customers by attribute")
        print("4. Find/edit a customer")
        print("5. Quit customers menu")
        selection = input("> ")
        if selection == "1":
            print("Please enter the required information below: ")
            name = input("Customer name:\n>")
            phone_number = input("Customer phone number:\n>")
            email = input("Customer email:\n>")
            address = input("Customer address:\n>")
            company_answer = input("Does this customer represent a company? (y/n)\n>")
            if company_answer.lower() in POSITIVE_ANSWERS:
                company_name = input("Please enter the name of the company:\n>")
            else:
                company_name = None
            insert_customer(name, phone_number, email, address, company_name)

        elif selection == "2":
            customers = get_all_customers()
            for customer in customers:
                print(customer)

        elif selection == "3":
            customers_dict = find_customers("Choose an attribute to view customers by")
            if customers_dict:
                print("Customers found:")
                for customer in customers_dict.values():
                    print(customer, ("\n" + ("----------" * 15)))
            else:
                print("The value entered had no matches.")

        elif selection == "4":
            customers_dict = find_customers("Choose an attribute to search for a customer by")
            if customers_dict:
                if customers_dict:
                    print("Customers found:")
                    for customer in customers_dict.values():
                        print(customer, ("\n" + ("----------" * 15)))
                    print("Choose a customer by their id in the list below:")
                    for index, customer in enumerate(customers_dict.values()):
                        print(f"{index+1}. {customer._id}")
                    chosen_customer = customers_dict[int(input(">"))]
                    print(chosen_customer, ("\n" + ("----------" * 15)))
                    while True:
                        answer = input("Do you want to edit an attribute? (y/n)\n>")
                        print(answer)
                        if answer.lower() in POSITIVE_ANSWERS:
                            chosen_attribute = input(f"Choose an attribute to edit:\n"
                                                     "1. Name\n"
                                                     "2. Phone Number\n"
                                                     "3. Email\n"
                                                     "4. Address\n"
                                                     "5. Company Name\n>")
                            if chosen_attribute in ["1", "1."]:
                                new_customer_name = input("Enter a new customer name:\n>")
                                change_customer_attribute(chosen_customer._id, "name", new_customer_name)

                            elif chosen_attribute in ["2", "2."]:
                                new_customer_phone_number = input("Enter a new customer phone number:\n>")
                                change_customer_attribute(chosen_customer._id, "phone_number", new_customer_phone_number)

                            elif chosen_attribute in ["3", "3."]:
                                new_customer_email = input("Enter a new customer email:\n>")
                                change_customer_attribute(chosen_customer._id, "email", new_customer_email)

                            elif chosen_attribute in ["4", "4."]:
                                new_customer_address = input("Enter a new customer address:\n>")
                                change_customer_attribute(chosen_customer._id, "address", new_customer_address)

                            elif chosen_attribute in ["5", "5."]:
                                new_customer_company_name = input("Enter a new customer company name:\n>")
                                change_customer_attribute(chosen_customer._id, "company_name", new_customer_company_name)
                        else:
                            break;
            else:
                print("The value entered had no matches.")

        elif selection == "5":
            break


def find_customers(prompt_message):
    chosen_attribute = input(f"{prompt_message}:\n"
                             "1. Name\n"
                             "2. Phone Number\n"
                             "3. Email\n"
                             "4. Address\n"
                             "5. Company Name\n>")
    if chosen_attribute in ["1", "1."]:
        customer_name = input("Enter customer name:\n>")
        return get_all_customers_by_attribute("name", customer_name)

    elif chosen_attribute in ["2", "2."]:
        customer_phone_number = input("Enter customer phone number:\n>")
        return get_all_customers_by_attribute("phone_number", customer_phone_number)

    elif chosen_attribute in ["3", "3."]:
        customer_email = input("Enter customer email:\n>")
        return get_all_customers_by_attribute("email", customer_email)

    elif chosen_attribute in ["4", "4."]:
        customer_address = input("Enter customer address:\n>")
        return get_all_customers_by_attribute("address", customer_address)

    elif chosen_attribute in ["5", "5."]:
        customer_company_name = input("Enter customer company name:\n>")
        return get_all_customers_by_attribute("company_name", customer_company_name)
