from config import get_settings
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

settings = get_settings()

#Database 
DATABASE = settings.DATABASE_URL.get_secret_value() #postgres database eventually 



#create the engine 
engine = create_engine(
    url = DATABASE,
    pool_pre_ping= True, #will query the data base to wait it up when its goes idle after inactivity
    pool_recycle= 300, #300s = 5 mins, scraps queries that are alive longer than 5 mins and then requiries them 
    
      )

#
class Base(DeclarativeBase):
    #initilize this
    #any models that inherits base will be registered as a database model 
    # Creates and manages a metadata object, accessible with Base.metadata 
    pass


#create the session factory 
SessionLocal = sessionmaker( 
    bind = engine,
    autoflush = False, #SQLAlchemy may send pending INSERT/UPDATE/DELETE statements to the database before a query so that the query sees the latest in-session state
    expire_on_commit=False # holds all the values in memory, if true then it creates a new select statmetn to get that data from data into memory. after commit(), SQLAlchemy keeps the ORM object attributes available in memory instead of marking them as expired and potentially re-querying the database when you access them.
    )

#yield db per request
def get_db() -> Generator[Session, None,None]:  #generator[yieldtype, sendtype, returntype]
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

