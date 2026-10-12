from enum import StrEnum
from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column
# from database import Base


class UserRoles(StrEnum):
    EMPLOYEE = "employee"
    TECHNICIAN = "technician"
    
from sqlalchemy.orm import DeclarativeBase #dlete

class Base(DeclarativeBase): #delete after expreiment
    pass

class User(Base):
# class User(Base):

    __tablename__ = "users"
    #id, username, Role, username, password

    id: Mapped[int] =  mapped_column(primary_key= True)
    name: Mapped[str] = mapped_column(String(length=50))
    role : Mapped[UserRoles] = mapped_column(Enum(UserRoles))
    username: Mapped[str] = mapped_column(String(50), unique = True)
    _password_hash: Mapped[str] = mapped_column(String(255) , name= "password_hash",) #don't name it password

    
from sqlalchemy.schema import CreateTable
from sqlalchemy.dialects import postgresql

#inspect ddl 
ddl = CreateTable(User.__table__).compile(dialect= postgresql.dialect())
print(ddl)

    

