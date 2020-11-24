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


def get_all_contacts_with_name(name):
    return session.query(Contact).filter(Contact.Name.like(f"%{name}%"))


def get_contact_by_name(name):
    return session.query(Contact).filter(Contact.Name == name).first()


def change_contact_name(contact, new_name):
    try:
        contact.Name = new_name
        session.commit()
    except:
        session.rollback()