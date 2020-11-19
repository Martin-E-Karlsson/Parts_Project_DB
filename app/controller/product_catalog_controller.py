import model.repository.product_catalog_repo as pcr


def insert_product_catalog(id_product, id_retailer):
    pcr.insert_product_catalog(id_product, id_retailer)


def get_all_product_catalogs():
    return pcr.get_all_product_catalogs()


def get_product_catalog_by_product_id(id_product):
    return pcr.get_product_catalog_by_product_id(id_product)


def get_product_catalogs_by_retailer_id(id_retailer):
    product_catalogs = pcr.get_product_catalogs_by_retailer_id(id_retailer)
    return {i+1: product_catalog for i, product_catalog in enumerate(product_catalogs)}

