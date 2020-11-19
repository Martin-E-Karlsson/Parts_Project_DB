import model.repository.company_repo as cr


def insert_company(company_name):
    cr.insert_company(company_name)


def get_all_companies():
    return cr.get_all_companies()


def get_company_by_id(id_company):
    return cr.get_company_by_id(id_company)


def get_company_by_name(company_name):
    companies = cr.get_company_by_name(company_name)
    return {i+1: company for i, company in enumerate(companies)}


def change_company_name(company, new_company_name):
    cr.change_company_name(company, new_company_name)
