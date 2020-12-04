from . import session
from model.models.mysql_db import Manufacturer, Customer, Car, Source, Contact, Company, Order, Store, Employee
import model.models.manufacturers as ma
import model.models.stores as st
import model.models.customers as cu


def fix_manufacturers():
    manufacturers = session.query(Manufacturer).all()
    for manufacturer in manufacturers:
        as_dict = manufacturer.__dict__
        as_dict['_id'] = int(as_dict['idManufacturer'])
        as_dict['hq_address'] = str(as_dict['HQAdress'])
        as_dict['hq_phone_number'] = str(as_dict['HQPhoneNumber'])
        as_dict['name'] = str(as_dict['ManufacturerName'])
        del as_dict['_sa_instance_state']
        del as_dict['idManufacturer']
        del as_dict['HQAdress']
        del as_dict['HQPhoneNumber']

        mongo_manufacturer = ma.Manufacturer(as_dict)
        mongo_manufacturer.insert()


def fix_customers():
    customers = session.query(Customer).all()
    cars = session.query(Car).all()
    orders = session.query(Order).all()
    for customer in customers:
        as_dict = customer.__dict__
        as_dict['_id'] = int(as_dict['idCustomer'])
        contact = session.query(Contact).filter(Contact.idContact == customer.idContact).first()
        as_dict['name'] = contact.Name
        as_dict['phone_number'] = contact.PhoneNumber
        as_dict['email'] = contact.Email
        if contact.idCompany:
            as_dict['company_name'] = session.query(Company).filter(
                Company.idCompany == contact.idCompany).first().CompanyName
        as_dict['address'] = str(as_dict['Address'])
        as_dict['cars'] = []
        for car in cars:
            car_as_dict = car.__dict__.copy()
            if car_as_dict['idCustomer'] == as_dict['_id']:
                car_as_dict['_id'] = car_as_dict['idCar']
                car_as_dict['model'] = car_as_dict['Model']
                car_as_dict['year'] = car_as_dict['ModelYear']
                car_as_dict['reg_number'] = car_as_dict['RegNumber']
                car_as_dict['manufacturer_id'] = session.query(Source).filter(
                    Source.idSource == car.idSource).first().idManufacturer
                del car_as_dict['_sa_instance_state']
                del car_as_dict['idCar']
                del car_as_dict['Model']
                del car_as_dict['ModelYear']
                del car_as_dict['Color']
                del car_as_dict['RegNumber']
                del car_as_dict['idCustomer']
                del car_as_dict['idSource']
                as_dict['cars'].append(car_as_dict)
        as_dict['orders'] = [order.idOrder for order in orders if as_dict['_id'] == order.idCustomer]
        del as_dict['_sa_instance_state']
        del as_dict['Address']
        del as_dict['idCustomer']
        del as_dict['idContact']

        mongo_customer = cu.Customer(as_dict)
        mongo_customer.insert()


def fix_stores():
    stores = session.query(Store).all()
    for store in stores:
        as_dict = store.__dict__
        as_dict['_id'] = int(as_dict['idStore'])
        as_dict['name'] = str(as_dict['Name'])
        as_dict['store_type'] = str(as_dict['StoreType'])
        employees = []
        for emp in store.employee:
            employees.append({
                'name': str(emp.Name),
                'phone_number': str(emp.PhoneNumber),
                'email': str(emp.Email),
                'orders': [order.idOrder for order in emp.orderdetail],
                '_id': int(emp.idEmployee)
            })
        as_dict['employees'] = employees.copy()

        as_dict['produckt_id'] = [p.idProduct for p in store.product]

        del as_dict['_sa_instance_state']
        del as_dict['Name']
        del as_dict['StoreType']
        del as_dict['idStore']
        del as_dict['product']
        del as_dict['employee']
        mongo_store = st.Store(as_dict)
        mongo_store.insert()
