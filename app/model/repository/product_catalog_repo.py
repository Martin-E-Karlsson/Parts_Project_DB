from model.db import session
from model.models.product_catalog import ProductCatalog


def insert_product_catalog(id_product, id_retailer):
    new_product_catalog = ProductCatalog(idProduct=id_product, idRetailer=id_retailer)
    session.add(new_product_catalog)
    session.commit()


def get_all_product_catalogs():
    return session.query(ProductCatalog).all()


def get_product_catalog_by_product_id(id_product):
    return session.query(ProductCatalog).filter(ProductCatalog.idProduct == id_product).first()


def get_product_catalogs_by_retailer_id(id_retailer):
    return session.query(ProductCatalog).filter(ProductCatalog.idRetailer == id_retailer).first()
