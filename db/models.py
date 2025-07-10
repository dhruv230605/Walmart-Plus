# db/models.py
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProductTrend(Base):
    __tablename__ = 'product_trends'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    source = Column(String)
    trend_score = Column(Float)
    date = Column(Date)
    region = Column(String)
    event_type = Column(String) 