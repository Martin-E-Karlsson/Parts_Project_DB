from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Car(Base):
    __tablename__ = "car"

    idCar = sa.Column(sa.INTEGER, primary_key=True)
    Model = sa.Column(sa.VARCHAR(45), nullable=False)
    ModelYear = sa.Column(sa.VARCHAR(4), nullable=False)
    Color = sa.Column(sa.VARCHAR(45), nullable=False)
    RegNumber = sa.Column(sa.VARCHAR(32), nullable=False)
    idCustomer = sa.Column(sa.INTEGER, sa.ForeignKey("customer.idCustomer"))
    idSource = sa.Column(sa.INTEGER, sa.ForeignKey("source.idSource"))
    Customer = relationship("Customer", back_populates="car")
    Source = relationship("Source", back_populates="car")

    def __repr__(self):
        return f"{self.idCar}, {self.Model}, {self.ModelYear}, {self.Color}, {self.RegNumber}," \
               f"self.idCustomer, {self.idSource}"
