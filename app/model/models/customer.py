from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = "customers"

    idCustomer = sa.Column(sa.Integer, primary_key=True)
    Address = sa.Column(sa.String(45), nullable=False)
    idContact = sa.Column(sa.Integer, sa.ForeignKey("contacts.idContact"), nullable=False)

    Car_owner = relationship("Car", back_populates='Customer')

    Contacts = relationship("Contact", back_populates="Customers")
    Orders = relationship("Order", back_populates="Customers")

    def __repr__(self):
        return f"{self.idCustomer},has address {self.Address}"
