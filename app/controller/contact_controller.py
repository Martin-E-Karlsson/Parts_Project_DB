import model.repository.contact_repo as cr


def insert_contact(name, phone_number, email, id_company=None):
    cr.insert_contact(name, phone_number, email, id_company)


def get_all_contacts():
    return cr.get_all_contacts()


def get_contact_by_id(id_contact):
    return cr.get_contact_by_id(id_contact)


def get_all_contacts_with_name(name):
    contacts = cr.get_all_contacts_with_name(name)
    return {i+1: contact for i, contact in enumerate(contacts)}


def get_contact_by_name(name):
    return cr.get_contact_by_name(name)


def change_contact_name(contact, new_name):
    cr.change_contact_name(contact, new_name)
