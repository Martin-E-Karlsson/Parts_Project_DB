from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class Company(Base):
    __tablename__ = "companies"

    idCompany = sa.Column(sa.Integer, primary_key=True)
    CompanyName = sa.Column(sa.String(45), nullable=False)

    Contacts = relationship("Contact", back_populates="Companies")



    def __repr__(self):
        return f"{self.idCompany}, {self.CompanyName}"
