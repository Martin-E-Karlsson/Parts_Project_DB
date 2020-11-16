from model.db import Base
import sqlalchemy as sa



class Manufacturer(Base):
    __tablename__ = "manufacturer"

    idManufacturer = sa.Column(sa.INTEGER, primary_key=True)
    HQAdress = sa.Column(sa.VARCHAR(45), nullable=False)
    HQPhoneNumber = sa.Column(sa.VARCHAR(45), nullable=False)
    Name = sa.Column(sa.VARCHAR(45), nullable=False)

    def __repr__(self):
        return f"{self.idManufacturer}, {self.HQAdress}, {self.HQPhoneNumber}, {self.Name}"
