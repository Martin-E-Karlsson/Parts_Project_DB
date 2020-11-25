from model.db import session
from model.models.car import Car


def insert_car(model, model_year, color, reg_number, id_source, id_customer):
    new_car = Car(
        Model=model,
        ModelYear=model_year,
        Color=color,
        RegNumber=reg_number,
        idSource=id_source,
        idCustomer=id_customer
    )
    session.add(new_car)
    session.commit()


def get_all_cars():
    return session.query(Car).all()


def get_car_by_id(id_car):
    return session.query(Car).filter(Car.idCar == id_car).first()


def get_all_cars_by_attribute(attribute_name, value):
    try:
        return session.query(Car).filter(getattr(Car, attribute_name).like(f"%{value}%")).all()
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_car_attribute(car, attribute_name, new_value):
    try:
        setattr(car, attribute_name, new_value)
        session.commit()
    except ValueError:
        print('Incorrect argument entered')
        session.rollback()
