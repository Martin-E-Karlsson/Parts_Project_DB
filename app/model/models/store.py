from model.db import Base
import sqlalchemy as sa
from model.models.employee import Employee
from sqlalchemy.orm import relationship


class Store(Base):
    __tablename__ = 'stores'

    idStore = sa.Column(sa.Integer, primary_key=True, nullable=False)
    Name = sa.Column(sa.String(100), nullable=False)
    StoreType = sa.Column(sa.String(100), nullable=False)

    employees = relationship("Employee", back_populates="Store")
    storeinventory = relationship("StoreInventory", back_populates="Store")

    def __repr__(self):
        return f"idStore={self.idStore}, Name={self.Name}, StoreType={self.StoreType}"
