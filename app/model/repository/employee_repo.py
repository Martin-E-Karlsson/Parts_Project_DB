from model.models.stores import Store


def insert_employee(name, email, phone_number, id_store, orders):
    if orders is None: orders = []
    Store.push_to_embedded_list(id_store, 'employees', {'name': name, 'phone_number': phone_number, 'email': email, 'orders': orders})


def get_all_employees():
    return [emp.employees for emp in Store.all()]


def get_employee_by_id(employee_id):
    print('This function is unavailable')


def get_all_employees_by_attribute(attribute_name, value):
    return [attribute for employee in Store.all()
            for attribute in employee.employees
            if attribute[attribute_name] == value]


def change_employee_attribute(store_id, attribute_name, new_value):
    value = Store.find(**{'_id' : store_id})[0].employees
    for i, e in enumerate(value):
        print(i, e)
    print('Select an employee to edit:')
    emp_id = input('>')
    value[int(emp_id)].update({attribute_name: new_value})
    Store.change_attribute(store_id, 'employees', value)

