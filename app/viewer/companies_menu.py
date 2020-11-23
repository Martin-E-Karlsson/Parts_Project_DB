from controller.company_controller import get_all_companies, insert_company, get_company_by_id
from controller.controller import store_changes


def companies_menu():
    while True:
        print("Companies menu")
        print("xxxxxxxx")
        print("1. Add a new customer")
        print("2. View all the companies")
        print("3. View company by id")
        print("4. View/edit company name")
        print("5. Quit company menu")
        selection = input("> ")
        if selection == "1":
            insert_company()
        elif selection == "2":
            companies = get_all_companies()
            for company in companies:
                print(company)
        elif selection == "3":
            id = input("Indicate company id: ")
            company = get_company_by_id(id)
            if company:
                print(company)
            else:
                print("Could not find a company with id", id)
        elif selection == "4":
            comp_name = input("Enter complete or partial name of the company: ")
            companies= get_company_by_id(comp_name)
            for key, company in companies.items():
                print(f"{key}.{companies}")
            edit_selection = input("Enter number for company to edit: ")
            edit_selection = int(edit_selection)

            company = companies[edit_selection]
            print(f" 1. Company name: {company.CompanyName}")
            company.CompanyName = input("Enter a new name: ")
            store_changes()
        elif selection == "5":
            break