import model.repository.car_repo as cr


def insert_car(customer_id, model, year, color, reg_number, manufacturer_id):
    cr.insert_car(customer_id, model, year, color, reg_number, manufacturer_id)


def get_all_cars():
    return cr.get_all_cars()


def get_car_by_id(car_id):
    return cr.get_car_by_id(car_id)


def get_all_cars_by_attribute(attribute_name, value):
    cars = cr.get_all_cars_by_attribute(attribute_name, value)
    return {i+1: car for i, car in enumerate(cars)}


def change_car_attribute(customer_id, attribute_name, new_value):
    cr.change_car_attribute(customer_id, attribute_name, new_value)
