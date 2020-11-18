from model.db import session
from model.models.car import Car


def insert_car(id_car, model, model_year, color, reg_number, id_customer=None, id_source=None):
    session.query(Car).add_column(idCar=id_car,
                                  Model=model,
                                  ModelYear=model_year,
                                  Color=color,
                                  RegNumber=reg_number,
                                  idCustomer=id_customer,
                                  idSource=id_source)


def get_all_cars():
    return session.query(Car).all()


def get_car_by_id(id_car):
    return session.query(Car).filter(Car.idCar == id_car).first()


def get_car_by_model(model):
    return session.query(Car).filter(Car.Model.like(model).all())
