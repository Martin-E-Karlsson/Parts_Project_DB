from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class ProductCatalog(Base):
    __tablename__ = "product_catalogs"

    idProduct = sa.Column(sa.Integer, sa.ForeignKey("products.idProduct"))
    idRetailer = sa.Column(sa.Integer, sa.ForeignKey("retailers.idRetailer"))
    Product = relationship("Product", back_populates = "ProductCatalogs")
    Retailer = relationship("Retailer", back_populates="ProductCatalogs")

    def __repr__(self):
        return f"{self.idProduct}, {self.Retailer}"