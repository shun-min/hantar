from .database import Base
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, List, String
from sqlalchemy.orm import relationship


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    size = Column(Float)
    directory = Column(String)
    file_name = Column(String)
    type = Column(String, u=True)
    locations = Column(List, u=True)
    mimetype = Column(String, u=True)
    version = relationship("Version", back_populates="dependencies")
    created_by = Column(DateTime)
    modified_by = Column(DateTime)
    created_date = Column(DateTime)
    modified_date = Column(DateTime)


class Version(Base):
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    dependencies = relationship("Item", back_populates="version")
    