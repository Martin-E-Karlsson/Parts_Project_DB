from model.db import session
from model.models.store import Store


def insert_store(name, store_type):
    new_store = Store(
        Name=name,
        StoreType=store_type
    )
    session.add(new_store)
    session.commit()


def get_all_stores():
    return session.query(Store).all()


def get_store_by_id(id_store):
    return session.query(Store).filter(Store.idStore == id_store).first()


def get_all_stores_by_attribute(attribute_name, value):
    try:
        return session.query(Store).filter(getattr(Store, attribute_name).like(f"%{value}%")).all()
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_store_attribute(store, attribute_name, new_value):
    try:
        setattr(store, attribute_name, new_value)
        session.commit()
    except ValueError:
        print('Incorrect argument entered')
        session.rollback()
