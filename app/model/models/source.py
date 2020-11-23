from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Source(Base):
    __tablename__ = "sources"

    idSource = sa.Column(sa.INTEGER, primary_key=True)
    idManufacturer = sa.Column(sa.INTEGER, sa.ForeignKey("manufacturers.idManufacturer"), nullable=False)

    Name_of_Manufacturer = relationship("Manufacturer", back_populates="Sources")
    car_origin = relationship("Car", back_populates="Sources")
    product_source = relationship("Product", back_populates="Source_of_product")


    def __repr__(self):
        return f"{self.idSource}, {self.ManufacturerName}"
