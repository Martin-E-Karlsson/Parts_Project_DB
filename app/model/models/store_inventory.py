from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class StoreInventory(Base):
    __tablename__ = 'storeinventorys'

    temp = sa.Column(sa.INTEGER, primary_key=True)
    #idProduct = sa.Column(sa.Integer, sa.ForeignKey('product.idProduct'), primary_key=True, nullable=False)
    #idStore = sa.Column(sa.Integer, sa.ForeignKey('store.idStore'), primary_key=True, nullable=False)

    Product = relationship("Product", back_populates="storeinventory")
    Store = relationship("Store", back_populates="storeinventory")

    def __repr__(self):
        return f"idProduct={self.idProduct}, idStore={self.idStore}"
