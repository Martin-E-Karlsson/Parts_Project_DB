from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class StoreInventory(Base):
    __tablename__ = 'storeinventorys'

    idProduct = sa.Column(sa.Integer, sa.ForeignKey('products.idProduct'), primary_key=True, nullable=False)
    idStore = sa.Column(sa.Integer, sa.ForeignKey('stores.idStore'), primary_key=True, nullable=False)

    Product = relationship("Product", back_populates="storeinventory")
    Store = relationship("Store", back_populates="storeinventory")

    def __repr__(self):
        return f"idProduct={self.idProduct}, idStore={self.idStore}"
