from enum import StrEnum
from sqlalchemy import String, Text
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column
# from database import Base


class UserRoles(StrEnum):
    EMPLOYEE = "employee"  #using auto() will cause issues if we changed the 
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
    role : Mapped[UserRoles] = mapped_column(SQLEnum(UserRoles,
                                                    values_callable=lambda obj: [e.value for e in obj],
                                                    native_enum=False,
                                                    create_constraint = True,
                                                    name = "user_roles")
                                                    )
    username: Mapped[str] = mapped_column(String(50), unique = True)
    password_hash: Mapped[str] = mapped_column(Text ) #Text we can limit the amount on the uuser input side before reaching database 
    
from sqlalchemy.schema import CreateTable
from sqlalchemy.dialects import postgresql

#inspect ddl 
ddl = CreateTable(User.__table__).compile(dialect= postgresql.dialect())
print(ddl)

print(User.__table__.c.role.type.enums)

