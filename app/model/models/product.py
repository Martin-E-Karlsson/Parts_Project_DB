from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

from model.models.product_catalog import ProductCatalog
from model.models.store_inventory import StoreInventory

class Product(Base):
    __tablename__ = "products"

    idProduct = sa.Column(sa.INTEGER, primary_key=True)
    Name = sa.Column(sa.String(45), nullable=False)
    Retailer = sa.Column(sa.String(45), nullable=False)
    Description = sa.Column(sa.String(45), nullable=False)
    PurchaseCost = sa.Column(sa.INTEGER, nullable=False)
    SellPrice = sa.Column(sa.INTEGER, nullable=False)
    idSource = sa.Column(sa.INTEGER, sa.ForeignKey("sources.idSource"), nullable=False)
    idWarehouse = sa.Column(sa.INTEGER, sa.ForeignKey("warehouses.idWarehouse"), nullable=False)


    ProductCatalogs = relationship("ProductCatalog", back_populates="Product")
    orderdetails = relationship("OrderDetails", back_populates="Product")
    Source_of_product = relationship("Source", back_populates="product_source")
    storeinventory = relationship("StoreInventory", back_populates="Product")


    def __repr__(self):
        return f"{self.idProduct}, {self.Name}, {self.Retailer}, {self.Description}, {self.PurchaseCost}, " \
               f"{self.SellPrice}, self.idSource, {self.idWarehouse}"
