from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Contact(Base):
    __tablename__ = "contacts"

    idContact = sa.Column(sa.Integer, primary_key=True)
    Name = sa.Column(sa.String(45), nullable=False)
    PhoneNumber = sa.Column(sa.String(45), nullable=False)
    Email = sa.Column(sa.String(45), nullable=False)
    idCompany = sa.Column(sa.Integer, sa.ForeignKey("companies.idCompany"))

    Customers = relationship("Customer", back_populates="Contacts")
    Companies = relationship("Company", back_populates="Contacts")


    def __repr__(self):
        return f"{self.idContact}, {self.Name}, {self.PhoneNumber}, {self.Email}"
