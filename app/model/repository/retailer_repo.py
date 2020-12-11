from model.models.retailers import Retailer


def insert_retailer(name, address, id_contact=None, id_manufacturer=None):
    new_retailer = Retailer({"name": name, "address": address, "id_contact": id_contact, "id_manufacturer": id_manufacturer})
    new_retailer.save()



def get_all_retailers():
    return Retailer.all()


def get_retailer_by_id(id_retailer):
    return Retailer.find(_id=id_retailer)


def get_all_retailers_by_attribute(attribute_name, value):
    try:
        return Retailer.find(**{attribute_name:value})
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_retailer_attribute(retailer_id, attribute_name, new_value):
    try:
        Retailer.change_attribute(retailer_id, attribute_name, new_value)
    except ValueError:
        print('Incorrect argument entered')

def insert_retailer_to_manufacturer(retailer_id, manufacturer_name, manufacturer_id):
    Retailer.push_to_embedded_list(retailer_id, 'manufacturers',{'manufacturer_name': manufacturer_name, 'manufacturer_id':manufacturer_id})


