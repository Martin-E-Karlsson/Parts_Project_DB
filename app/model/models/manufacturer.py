from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Manufacturer(Base):
    __tablename__ = "manufacturers"

    idManufacturer = sa.Column(sa.INTEGER, primary_key=True)
    HQAdress = sa.Column(sa.String(45), nullable=False)
    HQPhoneNumber = sa.Column(sa.String(45), nullable=False)
    ManufacturerName = sa.Column(sa.String(155), nullable=False)

    Sources = relationship("Source", back_populates="Name_of_Manufacturer")
    Parts = relationship("Retailer", back_populates="Manufacturer")

    def __repr__(self):
        return f"{self.idManufacturer}, {self.HQAdress}, {self.HQPhoneNumber}, {self.ManufacturerName}"
