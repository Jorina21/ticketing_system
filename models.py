from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class UserRoles(str, Enum):
    EMPLOYEE = "employee"
    TECHNICIAN = "technician"
    pass

class User(Base):


    #id, username, Role, username, password

    id: Mapped[int] =  mapped_column(primary_key= True)
    User_name: Mapped[str] = mapped_column(String(length=50))
    role : Mapped[UserRoles] = mapped_column(Enum(UserRoles))
    username: Mapped[str] = mapped_column(String(50), unique = True)
    hashed_password: Mapped[str] = mapped_column(String(255)) #don't name it password

    


    