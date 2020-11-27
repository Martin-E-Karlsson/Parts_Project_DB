from model.db import session
from model.models.contact import Contact


def insert_contact(name, phone_number, email, id_company=None):
    new_contact = Contact(
        Name=name,
        PhoneNumber=phone_number,
        Email=email,
        idCompany=id_company
    )
    session.add(new_contact)
    session.commit()


def get_all_contacts():
    return session.query(Contact).all()


def get_contact_by_id(id_contact):
    return session.query(Contact).filter(Contact.idContact == id_contact).first()


def get_all_contacts_by_attribute(attribute_name, value):
    try:
        return session.query(Contact).filter(getattr(Contact, attribute_name).like(f"%{value}%")).all()
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_contact_attribute(contact, attribute_name, new_value):
    try:
        setattr(contact, attribute_name, new_value)
        session.commit()
    except ValueError:
        print('Incorrect argument entered')
        session.rollback()