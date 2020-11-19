import model.repository.source_repo as sr


def insert_source(manufacturer_id):
    sr.insert_source(manufacturer_id)


def get_all_sources():
    return sr.get_all_sources()


def get_source_by_manufacturer_id(manufacturer_id):
    return sr.get_source_by_manufacturer_id(manufacturer_id)


def change_source_manufacturer_id(source, new_manufacturer_id):
    sr.change_source_manufacturer_id(source, new_manufacturer_id)
