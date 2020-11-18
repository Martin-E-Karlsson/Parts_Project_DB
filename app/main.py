from model.db import Base, engine, session
from model.models.warehouse import Warehouse
from model.models.product import Product
from model.models.car import Car
from model.models.source import Source
from model.models.manufacturer import Manufacturer
from model.models.company import Company
from model.models.contact import Contact
from model.models.employee import Employee
from model.models.order import Order
from model.models.order_details import OrderDetails
from model.models.retailer import Retailer
from model.models.store import Store
from model.models.store_inventory import StoreInventory



def main():
    Base.metadata.create_all(engine)



if __name__ == '__main__':
    main()
