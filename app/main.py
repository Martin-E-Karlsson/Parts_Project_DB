from model.db import Base, engine, session
from model.models.warehouse import Warehouse
from model.models.product import Product
from model.models.car import Car
from model.models.source import Source
from model.models.manufacturer import Manufacturer



def main():
    Base.metadata.create_all(engine)



if __name__ == '__main__':
    main()
