from model.db import session
from model.models.product_catalog import ProductCatalog


def insert_product_catalog(id_product, id_retailer):
    new_product_catalog = ProductCatalog(
        idProduct=id_product,
        idRetailer=id_retailer
    )
    session.add(new_product_catalog)
    session.commit()


def get_all_product_catalogs():
    return session.query(ProductCatalog).all()


def get_all_product_catalogs_by_attribute(attribute_name, value):
    try:
        return session.query(ProductCatalog).filter(getattr(ProductCatalog, attribute_name).like(f"%{value}%")).all()
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_product_catalog_attribute(product_catalog, attribute_name, new_value):
    try:
        setattr(product_catalog, attribute_name, new_value)
        session.commit()
    except ValueError:
        print('Incorrect argument entered')
        session.rollback()