import model.repository.employee_repo as er


def insert_employee(name, email, phone_number, id_store):
    er.insert_employee(name, email, phone_number, id_store)


def get_all_employees():
    return er.get_all_employees()


def get_employee_by_id(id_employee):
    return er.get_employee_by_id(id_employee)


def get_all_employees_with_name(name):
    employees = er.get_all_employees_with_name(name)
    return {i+1: employee for i, employee in enumerate(employees)}


def change_employee_name(employee, new_name):
    er.change_employee_name(employee, new_name)
