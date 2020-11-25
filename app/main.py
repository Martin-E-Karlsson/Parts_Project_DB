from model.db import Base, engine, session
from model.models.employee import Employee
from model.models.car import Car
from model.models.manufacturer import Manufacturer
from model.models.source import Source
from model.models.warehouse import Warehouse
from model.models.product import Product
from model.models.company import Company
from model.models.contact import Contact
from model.models.order import Order
from model.models.order_details import OrderDetails
from model.models.retailer import Retailer
from model.models.store import Store
from model.models.customer import Customer
from model.models.product_catalog import ProductCatalog
from model.models.store_inventory import StoreInventory

from viewer.store_menu import store_menu


def main():
    Base.metadata.create_all(engine)
    store_menu()

if __name__ == '__main__':
    main()
