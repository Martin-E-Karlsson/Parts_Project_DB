import model.repository.car_repo as cr


def insert_car(model, model_year, color, reg_number, id_source=None, id_customer=None):
    cr.insert_car(model, model_year, color, reg_number, id_source, id_customer)


def get_all_cars():
    return cr.get_all_cars()


def get_car_by_id(id_car):
    return cr.get_car_by_id(id_car)


def get_all_cars_by_attribute(attribute_name, value):
    cars = cr.get_all_cars_by_attribute(attribute_name, value)
    return {i+1: car for i, car in enumerate(cars)}


def change_car_attribute(car, attribute_name, new_value):
    cr.change_car_attribute(car, attribute_name, new_value)
