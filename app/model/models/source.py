from model.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relation


class Source(Base):
    __tablename__ = "source"

    idSource = sa.Column(sa.INTEGER, primary_key=True)
    ManufacturerName = sa.Column(sa.VARCHAR(255), nullable=False)

    def __repr__(self):
        return f"{self.idSource}, {self.ManufacturerName}"
