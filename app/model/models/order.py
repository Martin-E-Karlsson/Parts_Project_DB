from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = "orders"

    idOrder = sa.Column(sa.Integer, primary_key=True)
    idCustomer = sa.Column(sa.Integer, sa.ForeignKey("customers.idCustomer"))

    orderdetails = relationship("OrderDetails", back_populates="Order")
    Customers = relationship("Customer", back_populates="Orders")

    def __repr__(self):
        return f"{self.idOrder}"
