import model.repository.product_catalog_repo as pcr


def insert_product_catalog(id_product, id_retailer):
    pcr.insert_product_catalog(id_product, id_retailer)


def get_all_product_catalogs():
    return pcr.get_all_product_catalogs()


def get_all_product_catalogs_by_attribute(attribute_name, value):
    product_catalogs = pcr.get_all_product_catalogs_by_attribute(attribute_name, value)
    return {i+1: product_catalog for i, product_catalog in enumerate(product_catalogs)}


def change_product_catalog_attribute(product_catalog, attribute_name, new_value):
    pcr.change_product_catalog_attribute(product_catalog, attribute_name, new_value)
