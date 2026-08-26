from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


#Database 
DATABASE = " "




#create the engine
engine = create_engine(
    url = DATABASE,
    connect_args = {"check_same_thread": False}
    
      )

#
class Base(DeclarativeBase):
    #initilize this
    pass


#create the session factory 
SessionLocal = sessionmaker( 
    bind = engine,
    )

#yield db per request
def get_db() -> Generator[session, None,None]:  #generator[yieldtype, sendtype, returntype]
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#READ THE FIRST PROMPT IN CLAUDE ABOUT SQLITE
