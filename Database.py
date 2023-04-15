from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///akcie.db', echo=True)
Base = declarative_base()

class Akce(Base):
    __tablename__ = 'akce'
    id = Column(Integer, primary_key=True)
    nazev_akcie = Column(String)
    mena = Column(String)
    pocet_kusu = Column(Integer)
    broker = Column(String)
    datum = Column(Date)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()