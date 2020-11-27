from model.db import session
from model.models.product import Product


def insert_product(name, retailer, description, purchase_cost, sell_price, id_source, id_warehouse):
    new_product = Product(
        Name=name,
        Retailer=retailer,
        Description=description,
        PurchaseCost=purchase_cost,
        SellPrice=sell_price,
        idSource=id_source,
        idWarehouse=id_warehouse
    )
    session.add(new_product)
    session.commit()


def get_all_products():
    return session.query(Product).all()


def get_product_by_id(id_product):
    return session.query(Product).filter(Product.idProduct == id_product).first()


def get_all_products_by_attribute(attribute_name, value):
    try:
        return session.query(Product).filter(getattr(Product, attribute_name).like(f"%{value}%")).all()
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_product_attribute(product, attribute_name, new_value):
    try:
        setattr(product, attribute_name, new_value)
        session.commit()
    except ValueError:
        print('Incorrect argument entered')
        session.rollback()
