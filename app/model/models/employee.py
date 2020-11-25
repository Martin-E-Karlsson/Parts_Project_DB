from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Employee(Base):
    __tablename__ = "employees"

    idEmployee = sa.Column(sa.Integer, primary_key=True, nullable=False)
    Name = sa.Column(sa.String(100), nullable=False)
    Email = sa.Column(sa.String(100), nullable=False)
    PhoneNumber = sa.Column(sa.String(100), nullable=False)
    idStore = sa.Column(sa.Integer, sa.ForeignKey("stores.idStore"), nullable=False)

    orderdetails = relationship("OrderDetails", back_populates="Employee")
    Store = relationship("Store", back_populates="employees")

    def __repr__(self):
        return f"idEmployee={self.idEmployee}, Name={self.Name}, Email={self.Email}, PhoneNumber={self.PhoneNumber}, " \
               f"idStore={self.idStore}"
