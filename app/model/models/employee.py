from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Employee(Base):
    __tablename__ = "employee"

    idEmployee = sa.Column(sa.Integer, primary_key=True, nullable=False)
    Name = sa.Column(sa.String(100), nullable=False)
    Email = sa.Column(sa.String(100), nullable=False)
    PhoneNumber = sa.Column(sa.String(100), nullable=False)
    idStore = sa.Column(sa.Integer, sa.ForeignKey("store.idStore"), nullable=False)
    Store = relationship("Store", back_populates="employee")

    def __repr__(self):
        return f"idEmployee={self.idEmployee}, Name={self.Name}, Email={self.Email}, PhoneNumber={self.PhoneNumber}, " \
               f"idStore={self.idStore}"
