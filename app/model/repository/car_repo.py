from model.models.customers import Customer


def insert_car(customer_id, model, year, color, reg_number, manufacturer_id):
    Customer.push_to_embedded_list(
        customer_id,
        'cars',
        {
            'model': model,
            'year': year,
            'color': color,
            'reg_number': reg_number,
            'manufacturer_id': manufacturer_id,
        }
    )

def get_all_cars():
    car_list = [[car for car in customer.cars] for customer in Customer.all() if customer.cars]
    return [car for sub_list in car_list for car in sub_list]


def get_car_by_id(car_id):
    print("Function does not exist.")


def get_all_cars_by_attribute(attribute_name, value):
    return [attribute for car in Customer.all()
            for attribute in car.cars
            if attribute[attribute_name] == value]


def change_car_attribute(car, attribute_name, new_value):
    value = Customer.find(**{'cars': car})[0].cars
    value[0].update({attribute_name: new_value})
    Customer.change_attribute(Customer.find(**{'cars': car})[0]._id, 'cars', value)
