import model.repository.car_repo as cr


def insert_car(model, model_year, color, reg_number, id_customer=None, id_source=None):
    cr.insert_car(model, model_year, color, reg_number, id_customer, id_source)


def get_all_cars():
    return cr.get_all_cars()


def get_car_by_id(id_car):
    return cr.get_car_by_id(id_car)


def get_car_by_model(model):
    cars = cr.get_car_by_model(model)
    return {i+1: car for i, car in enumerate(cars)}


def change_car_model(car, new_model):
    cr.change_car_model(car, new_model)
