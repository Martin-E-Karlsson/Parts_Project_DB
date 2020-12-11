from controller.car_controller import get_all_cars, get_car_by_id, get_all_cars_by_attribute,\
    change_car_attribute, insert_car


def cars_menu():
    while True:
        print("Cars menu")
        print("xxxxxxxx")
        print("1. Add a new car")
        print("2. View all the cars")
        print("3. View car by id")
        print("4. View/edit car by model")
        print("5. Quit cars menu")
        selection = input("> ")
        if selection == "1":
            model = input("Indicate the model of the car: ")
            year = input("Indicate the model_year of the car: ")
            color = input("Indicate the color of the car: ")
            reg_number = input("Indicate the reg_number of the car: ")
            customer_id = input("Indicate the customer_id of the car: ")
            manufacturer_id = input("Indicate the manufacturer_id of the car: ")
            insert_car(int(customer_id), model, year, color, reg_number, int(manufacturer_id))
        elif selection == "2":
            cars = get_all_cars()
            for car in cars:
                print(car)
        elif selection == "3":
            id_car = input("Indicate car id: ")
            car = get_car_by_id(id_car)
            if car:
                print(car)
            else:
                print("Could not find a car with id", id_car)
        elif selection == "4":
            model = input("Enter the model of the car: ")
            cars = get_all_cars_by_attribute("model", model)
            for key, car in cars.items():
                print(f"{key}.{car}")
            edit_selection = input("Enter number for the car to be edited: ")
            edit_selection = int(edit_selection)

            car = cars[edit_selection]
            print(f" 1. Car model: {car['model']}")
            new_model = input("Enter a new model: ")
            change_car_attribute(car, "model", new_model)
        elif selection == "5":
            break
