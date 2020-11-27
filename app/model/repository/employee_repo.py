from model.db import session
from model.models.employee import Employee


def insert_employee(name, email, phone_number, id_store):
    new_employee = Employee(
        Name=name,
        Email=email,
        PhoneNumber=phone_number,
        idStore=id_store
    )
    session.add(new_employee)
    session.commit()


def get_all_employees():
    return session.query(Employee).all()


def get_employee_by_id(id_employee):
    return session.query(Employee).filter(Employee.idEmployee == id_employee).first()


def get_all_employees_by_attribute(attribute_name, value):
    try:
        return session.query(Employee).filter(getattr(Employee, attribute_name).like(f"%{value}%")).all()
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_employee_attribute(employee, attribute_name, new_value):
    try:
        setattr(employee, attribute_name, new_value)
        session.commit()
    except ValueError:
        print('Incorrect argument entered')
        session.rollback()
