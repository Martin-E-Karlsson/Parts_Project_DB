from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relation


class Warehouse(Base):
    __tablename__ = "warehouse"

    idWarehouse = sa.Column(sa.INTEGER, primary_key=True)
    ProductInStorage = sa.Column(sa.INTEGER, nullable=False)
    MinimalAmountInStorage = sa.Column(sa.INTEGER, nullable=False)
    AmountToBeDelivered = sa.Column(sa.INTEGER, nullable=False)
    ProductDeliveryDate = sa.Column(sa.DATE)

    def __repr__(self):
        return f"{self.idWarehouse}, {self.ProductInStorage}, {self.MinimalAmountInStorage}, " \
               f"{self.AmountToBeDelivered}, {self.ProductDeliveryDate}"
