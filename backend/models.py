from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    steamid = Column(String, unique=True, nullable=False)

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class PriceHistory(Base):
    __tablename__ = 'price_history'
    id = Column(Integer, primary_key=True)
    item_name = Column(String, ForeignKey('items.name'))
    source = Column(String)  # steam or external
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    item = relationship('Item')

    def as_dict(self):
        return {
            'item_name': self.item_name,
            'source': self.source,
            'price': self.price,
            'created_at': self.created_at.isoformat(),
        }
