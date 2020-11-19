from model.db import session


def store_changes():
    session.commit()


def discard_changes():
    session.rollback()
