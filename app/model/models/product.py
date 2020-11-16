from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "product"

    idProduct = sa.Column(sa.INTEGER, primary_key=True)
    Name = sa.Column(sa.VARCHAR(45), nullable=False)
    Retailer = sa.Column(sa.VARCHAR(45), nullable=False)
    Description = sa.Column(sa.VARCHAR(45), nullable=False)
    PurchaseCost = sa.Column(sa.INTEGER, nullable=False)
    SellPrice = sa.Column(sa.INTEGER, nullable=False)
    idSource = sa.Column(sa.INTEGER, sa.ForeignKey("source.idSource"))
    idWarehouse = sa.Column(sa.INTEGER, sa.ForeignKey("warehouse.idWarehouse"))
    Source = relationship("Source", back_populates="product")


    def __repr__(self):
        return f"{self.idProduct}, {self.Name}, {self.Retailer}, {self.Description}, {self.PurchaseCost}, " \
               f"{self.SellPrice}, self.idSource, {self.idWarehouse}"
