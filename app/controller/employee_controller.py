import model.repository.employee_repo as er


def insert_employee(name, email, phone_number, id_store):
    er.insert_employee(name, email, phone_number, id_store)


def get_all_employees():
    return er.get_all_employees()


def get_employee_by_id(id_employee):
    return er.get_employee_by_id(id_employee)


def get_all_employees_by_attribute(attribute_name, value):
    employees = er.get_all_cars_by_attribute(attribute_name, value)
    return {i+1: employee for i, employee in enumerate(employees)}


def change_employee_attribute(employee, attribute_name, new_value):
    er.change_employee_attribute(employee, attribute_name, new_value)
