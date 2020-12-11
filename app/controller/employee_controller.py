import model.repository.employee_repo as er


def insert_employee(name, email, phone_number, id_store, orders=None):
    er.insert_employee(name, email, phone_number, id_store, orders)


def get_all_employees():
    return er.get_all_employees()


def get_employee_by_id(employee_id):
    return er.get_employee_by_id(employee_id)


def get_all_employees_by_attribute(attribute_name, value):
    employees = er.get_all_employees_by_attribute(attribute_name, value)
    return {i+1: employee for i, employee in enumerate(employees)}


def change_employee_attribute(store_id, attribute_name, new_value):
    er.change_employee_attribute(store_id, attribute_name, new_value)
