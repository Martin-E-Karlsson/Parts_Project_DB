from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

from model.models.product import Product

class OrderDetails(Base):
    __tablename__ = 'orderdetails'

    ProductQuantity = sa.Column(sa.Integer, nullable=False)
    PurchaseDate = sa.Column(sa.DATETIME, nullable=False)
    idOrder = sa.Column(sa.Integer, sa.ForeignKey('orders.idOrder'), primary_key=True, nullable=False)
    idProduct = sa.Column(sa.Integer, sa.ForeignKey('products.idProduct'), primary_key=True, nullable=False)
    idEmployee = sa.Column(sa.Integer, sa.ForeignKey('employees.idEmployee'), nullable=False)

    Product = relationship("Product", back_populates="orderdetails")
    Employee = relationship("Employee", back_populates="orderdetails")
    Order = relationship("Order", back_populates="orderdetails")


    def __repr__(self):
        return f"ProductQuantity={self.ProductQuantity}, PurchaseDate={self.PurchaseDate}, idOrder={self.idOrder}, " \
               f"idProduct={self.idProduct}, idEmployee={self.idEmployee}"
