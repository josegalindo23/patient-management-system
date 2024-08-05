import datetime
from sqlalchemy import Column, Integer, String, DateTime
from src.infrastructure.adapters.data_sources.db_config import Base, engine

class Patient_entity(Base):

    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    document = Column(String)
    date_of_birth = Column(DateTime)
    gender = Column(String)
    blood_type = Column(String)
    allergies = Column(String)

Base.metadata.create_all(bind=engine)