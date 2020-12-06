import datetime
from app.model.db import session
from app.model.models.mysql_db import Manufacturer, Product, t_product_catalogs,Retailer, Source, Warehouse
from app.model.models import manufacturers as ma
from app.model.models import products as p


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


