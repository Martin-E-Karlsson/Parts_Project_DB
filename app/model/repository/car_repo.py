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


def get_cars_by_model(model):
    return session.query(Car).filter(Car.Model.like(f"%{model}%").all())


def change_car_model(car, new_model):
    try:
        car.Model = new_model
        session.commit()
    except:
        session.rollback()
