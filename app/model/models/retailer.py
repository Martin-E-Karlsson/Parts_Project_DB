from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class Retailer(Base):
    __tablename__ = "retailers"

    idRetailer = sa.Column(sa.Integer, primary_key=True)
    Name = sa.Column(sa.String(45), nullable=False)
    Address = sa.Column(sa.String(45), nullable=False)
    idContact = sa.Column(sa.Integer, sa.ForeignKey("contacts.idContact"))
    idManufacturer = sa.Column(sa.Integer, sa.ForeignKey("manufacturers.idManufacturer"))
    Manufacturer = relationship("Retailer", back_populates = "Manufacturer")

    def __repr__(self):
        return f"{self.idRetailer},{self.Name}, {self.Address}"