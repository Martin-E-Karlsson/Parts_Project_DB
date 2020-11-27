from model.db import session
from model.models.company import Company


def insert_company(company_name):
    new_company = Company(CompanyName=company_name)
    session.add(new_company)
    session.commit()


def get_all_companies():
    return session.query(Company).all()


def get_company_by_id(id_company):
    return session.query(Company).filter(Company.idCompany == id_company).first()


def get_all_companies_by_attribute(attribute_name, value):
    try:
        return session.query(Company).filter(getattr(Company, attribute_name).like(f"%{value}%")).all()
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")


def change_company_attribute(company, attribute_name, new_value):
    try:
        setattr(company, attribute_name, new_value)
        session.commit()
    except ValueError:
        print('Incorrect argument entered')
        session.rollback()