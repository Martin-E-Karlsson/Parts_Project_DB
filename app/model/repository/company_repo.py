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


def get_companies_by_name(company_name):
    return session.query(Company).filter(Company.CompanyName.like(f"%{company_name}%").all())


def change_company_name(company, new_company_name):
    try:
        company.CompanyName = new_company_name
        session.commit()
    except:
        session.rollback()