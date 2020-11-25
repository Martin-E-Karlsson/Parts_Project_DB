from controller.employee_controller import insert_employee, get_all_employees, get_employee_by_id, get_employee_by_name, \
    change_employee_name


def emloyees_menu():
    while True:
        print("Employees menu")
        print("xxxxxxxx")
        print("1. Add a new employee")
        print("2. View all the employees")
        print("3. View employee by id")
        print("4. View/edit employee by name")
        print("5. Quit employees menu")
        selection = input("> ")
        if selection == "1":
            name = input("Write employee's name: ")
            email = input ("Write employee's email: ")
            phone_number = ("Write employee's phone number: ")
            id_store = ("Write employee's id_store: ")
            insert_employee(name, email, phone_number, id_store)
        elif selection == "2":
            employees = get_all_employees()
            for employee in employees:
                print(employee)
        elif selection == "3":
            id_employee = input("Indicate employee id: ")
            employee = get_employee_by_id(id_employee)
            if employee:
                print(employee)
            else:
                print("Could not find the employee id", id_employee)
        elif selection == "4":
            name = input("Enter complete or partial name: ")
            employees= get_employee_by_name(name)
            for key, employee in employees.items():
                print(f"{key}.{employee}")
            edit_selection = input("Enter number for employee to edit: ")
            edit_selection = int(edit_selection)

            employee = employees[edit_selection]
            print(f" 1. Employee name: {employee.Name}")
            new_name = input("Enter a new name: ")
            change_employee_name(employee, new_name)
        elif selection == "5":
            break
