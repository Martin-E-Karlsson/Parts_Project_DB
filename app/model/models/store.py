from model.db import Base
import sqlalchemy as sa


class Store(Base):
    __tablename__ = 'store'

    idStore = sa.Column(sa.Integer, primary_key=True, nullable=False)
    Name = sa.Column(sa.String(100), nullable=False)
    StoreType = sa.Column(sa.String(100), nullable=False)

    def __repr__(self):
        return f"idStore={self.idStore}, Name={self.Name}, StoreType={self.StoreType}"
