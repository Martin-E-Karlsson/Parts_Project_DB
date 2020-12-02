# coding: utf-8
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Company(Base):
    __tablename__ = 'companies'

    idCompany = Column(Integer, primary_key=True)
    CompanyName = Column(String(45), nullable=False)


class Manufacturer(Base):
    __tablename__ = 'manufacturers'

    idManufacturer = Column(Integer, primary_key=True)
    HQAdress = Column(String(45), nullable=False)
    HQPhoneNumber = Column(String(45), nullable=False)
    ManufacturerName = Column(String(155), nullable=False)


class Store(Base):
    __tablename__ = 'stores'

    idStore = Column(Integer, primary_key=True)
    Name = Column(String(100), nullable=False)
    StoreType = Column(String(100), nullable=False)


class Warehouse(Base):
    __tablename__ = 'warehouses'

    idWarehouse = Column(Integer, primary_key=True)
    ProductInStorage = Column(Integer, nullable=False)
    MinimalAmountInStorage = Column(Integer, nullable=False)
    AmountToBeDelivered = Column(Integer, nullable=False)
    ProductDeliveryDate = Column(Date)


class Contact(Base):
    __tablename__ = 'contacts'

    idContact = Column(Integer, primary_key=True)
    Name = Column(String(45), nullable=False)
    PhoneNumber = Column(String(45), nullable=False)
    Email = Column(String(45), nullable=False)
    idCompany = Column(ForeignKey('companies.idCompany'), index=True)

    company = relationship('Company')


class Employee(Base):
    __tablename__ = 'employees'

    idEmployee = Column(Integer, primary_key=True)
    Name = Column(String(100), nullable=False)
    Email = Column(String(100), nullable=False)
    PhoneNumber = Column(String(100), nullable=False)
    idStore = Column(ForeignKey('stores.idStore'), nullable=False, index=True)

    store = relationship('Store')


class Source(Base):
    __tablename__ = 'sources'

    idSource = Column(Integer, primary_key=True)
    idManufacturer = Column(ForeignKey('manufacturers.idManufacturer'), nullable=False, index=True)

    manufacturer = relationship('Manufacturer')


class Customer(Base):
    __tablename__ = 'customers'

    idCustomer = Column(Integer, primary_key=True)
    Address = Column(String(45), nullable=False)
    idContact = Column(ForeignKey('contacts.idContact'), nullable=False, index=True)

    contact = relationship('Contact')


class Product(Base):
    __tablename__ = 'products'

    idProduct = Column(Integer, primary_key=True)
    Name = Column(String(45), nullable=False)
    Retailer = Column(String(45), nullable=False)
    Description = Column(String(45), nullable=False)
    PurchaseCost = Column(Integer, nullable=False)
    SellPrice = Column(Integer, nullable=False)
    idSource = Column(ForeignKey('sources.idSource'), nullable=False, index=True)
    idWarehouse = Column(ForeignKey('warehouses.idWarehouse'), nullable=False, index=True)

    source = relationship('Source')
    warehouse = relationship('Warehouse')
    retailers = relationship('Retailer', secondary='product_catalogs')
    stores = relationship('Store', secondary='storeinventorys')


class Retailer(Base):
    __tablename__ = 'retailers'

    idRetailer = Column(Integer, primary_key=True)
    Name = Column(String(45), nullable=False)
    Address = Column(String(45), nullable=False)
    idContact = Column(ForeignKey('contacts.idContact'), index=True)
    idManufacturer = Column(ForeignKey('manufacturers.idManufacturer'), index=True)

    contact = relationship('Contact')
    manufacturer = relationship('Manufacturer')


class Car(Base):
    __tablename__ = 'cars'

    idCar = Column(Integer, primary_key=True)
    Model = Column(String(45), nullable=False)
    ModelYear = Column(String(4), nullable=False)
    Color = Column(String(45), nullable=False)
    RegNumber = Column(String(32), nullable=False)
    idSource = Column(ForeignKey('sources.idSource'), nullable=False, index=True)
    idCustomer = Column(ForeignKey('customers.idCustomer'), nullable=False, index=True)

    customer = relationship('Customer')
    source = relationship('Source')


class Order(Base):
    __tablename__ = 'orders'

    idOrder = Column(Integer, primary_key=True)
    idCustomer = Column(ForeignKey('customers.idCustomer'), index=True)

    customer = relationship('Customer')


t_product_catalogs = Table(
    'product_catalogs', metadata,
    Column('idProduct', ForeignKey('products.idProduct'), primary_key=True, nullable=False),
    Column('idRetailer', ForeignKey('retailers.idRetailer'), primary_key=True, nullable=False, index=True)
)


t_storeinventorys = Table(
    'storeinventorys', metadata,
    Column('idProduct', ForeignKey('products.idProduct'), primary_key=True, nullable=False),
    Column('idStore', ForeignKey('stores.idStore'), primary_key=True, nullable=False, index=True)
)


class Orderdetail(Base):
    __tablename__ = 'orderdetails'

    ProductQuantity = Column(Integer, nullable=False)
    PurchaseDate = Column(DateTime, nullable=False)
    idOrder = Column(ForeignKey('orders.idOrder'), primary_key=True, nullable=False)
    idProduct = Column(ForeignKey('products.idProduct'), primary_key=True, nullable=False, index=True)
    idEmployee = Column(ForeignKey('employees.idEmployee'), nullable=False, index=True)

    employee = relationship('Employee')
    order = relationship('Order')
    product = relationship('Product')
