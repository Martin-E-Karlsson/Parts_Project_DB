from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Car(Base):
    __tablename__ = "cars"

    idCar = sa.Column(sa.INTEGER, primary_key=True)
    Model = sa.Column(sa.String(45), nullable=False)
    ModelYear = sa.Column(sa.String(4), nullable=False)
    Color = sa.Column(sa.String(45), nullable=False)
    RegNumber = sa.Column(sa.String(32), nullable=False)

    idSource = sa.Column(sa.INTEGER, sa.ForeignKey('sources.idSource'), nullable=False)
    idCustomer = sa.Column(sa.INTEGER, sa.ForeignKey('customers.idCustomer'), nullable=False)

    Customer = relationship("Customer", back_populates="Car_owner")
    Sources = relationship("Source", back_populates="car_origin")

    def __repr__(self):
        return f"{self.idCar}, {self.Model}, {self.ModelYear}, {self.Color}, {self.RegNumber}," \
               f"{self.idCustomer}, {self.idSource}"
