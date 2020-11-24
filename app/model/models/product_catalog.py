from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

from model.models.retailer import Retailer

class ProductCatalog(Base):
    __tablename__ = "product_catalogs"

    idProduct = sa.Column(sa.Integer, sa.ForeignKey("products.idProduct"), primary_key=True)
    idRetailer = sa.Column(sa.Integer, sa.ForeignKey("retailers.idRetailer"), primary_key=True)

    Product = relationship("Product", back_populates="ProductCatalogs")
    Retailer = relationship("Retailer", back_populates="ProductCatalogs")

    def __repr__(self):
        return f"{self.idProduct}, {self.Retailer}"
