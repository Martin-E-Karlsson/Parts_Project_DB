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


def get_all_employees_with_name(name):
    return session.query(Employee).filter(Employee.Name.like(f"%{name}%").all())


def change_employee_name(employee, new_name):
    try:
        employee.Name = new_name
        session.commit()
    except:
        session.rollback()