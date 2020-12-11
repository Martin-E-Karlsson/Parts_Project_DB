from . import session
from model.models.mysql_db import *
import model.models.manufacturers as ma
import model.models.stores as st
import model.models.customers as cu
import model.models.orders as od
import model.models.retailers as rt
from model.models import products as p, retailers
import datetime


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
        as_dict['name'] = str(contact.Name)
        as_dict['phone_number'] = str(contact.PhoneNumber)
        as_dict['email'] = str(contact.Email)
        if contact.idCompany:
            as_dict['company_name'] = str(session.query(Company).filter(Company.idCompany == contact.idCompany).first().CompanyName)
        as_dict['address'] = str(as_dict['Address'])
        as_dict['cars'] = []
        for car in cars:
            car_as_dict = car.__dict__.copy()
            if car_as_dict['idCustomer'] == as_dict['_id']:
                car_as_dict['model'] = str(car_as_dict['Model'])
                car_as_dict['year'] = str(car_as_dict['ModelYear'])
                car_as_dict['color'] = str(car_as_dict['Color'])
                car_as_dict['reg_number'] = str(car_as_dict['RegNumber'])
                car_as_dict['manufacturer_id'] = session.query(Source).filter(Source.idSource == car.idSource).first().idManufacturer
                del car_as_dict['_sa_instance_state']
                del car_as_dict['idCar']
                del car_as_dict['Model']
                del car_as_dict['ModelYear']
                del car_as_dict['Color']
                del car_as_dict['RegNumber']
                del car_as_dict['idCustomer']
                del car_as_dict['idSource']
                as_dict['cars'].append(car_as_dict)
        as_dict['orders'] = [int(order.idOrder) for order in orders if as_dict['_id'] == order.idCustomer]
        del as_dict['_sa_instance_state']
        del as_dict['Address']
        del as_dict['idCustomer']
        del as_dict['idContact']

        mongo_customer = cu.Customer(as_dict)
        mongo_customer.insert()


def fix_orders():
    orders = session.query(Order).all()
    order_details = session.query(Orderdetail).all()
    for order in orders:
        as_dict = order.__dict__
        as_dict['_id'] = int(as_dict['idOrder'])
        as_dict['customer_id'] = int(as_dict['idCustomer'])
        as_dict['products'] = []
        for order_detail in order_details:
            if order_detail.idOrder == as_dict['_id']:
                product_as_dict = order_detail.__dict__.copy()
                product_as_dict['product_id'] = int(order_detail.idProduct)
                product_as_dict['order_date'] = order_detail.PurchaseDate
                product_as_dict['product_quantity'] = int(order_detail.ProductQuantity)
                product_as_dict['employee_id'] = int(order_detail.idEmployee)
                del product_as_dict['_sa_instance_state']
                del product_as_dict['ProductQuantity']
                del product_as_dict['PurchaseDate']
                del product_as_dict['idOrder']
                del product_as_dict['idProduct']
                del product_as_dict['idEmployee']
                as_dict['products'].append(product_as_dict)
        del as_dict['_sa_instance_state']
        del as_dict['idOrder']
        del as_dict['idCustomer']

        mongo_order = od.Order(as_dict)
        mongo_order.insert()


def fix_stores():
    stores = session.query(Store).all()
    for store in stores:
        as_dict = store.__dict__
        as_dict['_id'] = int(as_dict['idStore'])
        as_dict['name'] = str(as_dict['Name'])
        as_dict['store_type'] = str(as_dict['StoreType'])
        employees = []
        for employee in store.employee:
            employees.append({
                'name': str(employee.Name),
                'phone_number': str(employee.PhoneNumber),
                'email': str(employee.Email),
                'orders': [order.idOrder for order in employee.orderdetail],
                '_id': int(employee.idEmployee)
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
        

def fix_products():
    products = session.query(Product).all()
    product_catalogs = session.query(t_product_catalogs).all()

    for product in products:
        as_dict = product.__dict__
        as_dict['_id'] = as_dict['idProduct']
        as_dict['name'] = as_dict['Name']
        as_dict['sell_price'] = as_dict['SellPrice']
        as_dict['description'] = as_dict['Description']
        as_dict['purchase_cost'] = as_dict['PurchaseCost']
        del as_dict['PurchaseCost']
        del as_dict['Description']
        del as_dict['SellPrice']
        del as_dict['Name']
        del as_dict['idProduct']

        as_dict['retailers'] = []
        for product_catalog in product_catalogs:
            if as_dict['_id'] == product_catalog.idProduct:
                product_catalog_as_dict = {}
                product_catalog_as_dict['retailer_id'] = product_catalog.idRetailer
                product_catalog_as_dict['retailer_name'] = session.query(Retailer).filter(Retailer.idRetailer == product_catalog_as_dict['retailer_id']).first().Name
                as_dict['retailers'].append(product_catalog_as_dict)

        as_dict['manufacturer_id'] = session.query(Source).filter(Source.idSource == as_dict['idSource']).first().idManufacturer
        warehouse = session.query(Warehouse).filter(Warehouse.idWarehouse ==as_dict['idWarehouse']).first().__dict__
        as_dict['product_in_stock'] = warehouse['ProductInStorage']
        as_dict['minimal_stock_amount'] = warehouse['MinimalAmountInStorage']
        as_dict['amount_ordered'] = warehouse['AmountToBeDelivered']
        delivery_date = warehouse['ProductDeliveryDate']
        if delivery_date:
            as_dict['delivery_date'] = datetime.datetime(delivery_date.year, delivery_date.month, delivery_date.day)
        else:
            as_dict['delivery_date'] = None

        del as_dict['Retailer']
        del as_dict['idWarehouse']
        del as_dict['idSource']
        del as_dict['_sa_instance_state']
        mongo_product = p.Product(as_dict)
        mongo_product.insert()

def fix_retailers():
    retailers = session.query(Retailer).all()
    for retailer in retailers:
        as_dict = retailer.__dict__
        as_dict['_id'] = int(as_dict['idRetailer'])
        as_dict['name'] = str(as_dict['Name'])
        as_dict['address'] = str(as_dict['Address'])
        contacts = []
        contact_fix = []
        contact_fix.append(retailer.contact)

        for contact in contact_fix:
            print()
            contacts.append({
                'name': str(contact.Name),
                'phone_number': str(contact.PhoneNumber),
                'email': str(contact.Email)
            })
        as_dict['contacts'] = contacts.copy()
        as_dict['manufacturer_id'] = int(as_dict['idManufacturer'])

        del as_dict['Name']
        del as_dict['Address']
        del as_dict['idManufacturer']
        del as_dict['_sa_instance_state']
        del as_dict['idRetailer']
        del as_dict['idContact']
        del as_dict['contact']
        mongo_product = rt.Retailer(as_dict)
        mongo_product.insert()
