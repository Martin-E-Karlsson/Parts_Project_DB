from model.models.products import Product


def insert_product(name, description, purchase_cost, sell_price, product_in_stock, minimal_stock_amount, manufacturer_id, amount_ordered=None, delivery_date=None):
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



def get_all_products():
    return Product.all()


def get_product_by_id(id_product):
    return Product.find(_id=id_product)


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


def insert_retailer_to_product(product_id, retailer_name, retailer_id):
    Product.push_to_embedded_list(product_id, 'retailers',{'retailer_name': retailer_name, 'retailer_id':retailer_id})

