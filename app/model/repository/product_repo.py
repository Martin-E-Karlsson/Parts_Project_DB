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


def get_product_by_name(name):
    return session.query(Product).filter(Product.Name.like(f"%{name}%").all())


def change_product_name(product, new_name):
    try:
        product.Name = new_name
        session.commit()
    except:
        session.rollback()