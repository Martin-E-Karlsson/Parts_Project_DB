from model.models.products import Product
from bson import ObjectId


def insert_product(name, description, purchase_cost, sell_price, product_in_stock, minimal_stock_amount, manufacturer_id, amount_ordered, delivery_date):
    new_product = Product({
        'name': name,
        'description': description,
        'purchase_cost': purchase_cost,
        'sell_price': sell_price,
        'product_in_stock': product_in_stock,
        'minimal_stock_amount':minimal_stock_amount,
        'manufacturer_id': manufacturer_id,
        'amount_ordered': amount_ordered,
        'delivery_date': delivery_date,
        'retailers': []
    })
    new_product.save()


def get_all_products():
    return Product.all()


def get_product_by_id(product_id):
    if product_id.isdigit():
        return Product.find(**{'_id': int(product_id)})
    else:
        return Product.find(**{'_id': ObjectId(product_id)})


def get_all_products_by_attribute(attribute_name, value):
    try:
        return Product.find(**{attribute_name: value})
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_product_attribute(product_id, attribute_name, new_value):
    try:
        Product.change_attribute(product_id, attribute_name, new_value)
    except ValueError:
        print('Incorrect argument entered')


def add_retailer_to_product(product_id, retailer_name, retailer_id):
    Product.push_to_embedded_list(product_id, 'retailers',{'retailer_name': retailer_name, 'retailer_id':retailer_id})

