from controller.company_controller import get_all_companies, insert_company, get_company_by_id, change_company_name, \
    get_companies_by_name
from controller.controller import store_changes


def companies_menu():
    while True:
        print("Companies menu")
        print("xxxxxxxx")
        print("1. Add a new company")
        print("2. View all the companies")
        print("3. View company by id")
        print("4. View/edit company name")
        print("5. Quit company menu")
        selection = input("> ")
        if selection == "1":
            company_name = input("Write the name of the company: ")
            insert_company(company_name)
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
            company_name = input("Enter complete or partial name of the company: ")
            companies = get_companies_by_name(company_name)
            for key, company in companies.items():
                print(f"{key}.{companies}")
            edit_selection = input("Enter number for company to edit: ")
            edit_selection = int(edit_selection)

            company = companies[edit_selection]
            print(f" 1. Company name: {company.CompanyName}")
            new_company_name = input("Enter a new name: ")
            change_company_name(company, new_company_name)
        elif selection == "5":
            break