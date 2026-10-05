import bcrypt 

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, String

from database import Base


class User(Base):

    __tablename__ = "User"

    user_id: Mapped[int] = mapped_column(primary_key = True, index = True, nullable = False)
    name: Mapped[str] = mapped_column(String(100), nullable = False)
    role: Mapped[str] = mapped_column(String(100), nullable = False)
    username: Mapped[str] = mapped_column(String(100),nullable = False)
    _password_hash = mapped_column(String(128), nullable = False)

    @property
    def password(self): #prevents reading a plain text password
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, plain_text_password):

        #Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)

        #store the decoded string variant in the database
        self._password_hash = hashed.decode('utf-8')

    def check_password(self, plain_text_password):
        #verify password against the stored hash
        return bcrypt.check_pw(
                plain_text_password.encode('utf-8'),
                self._password_hash.encode('utf-8')
            )

#other table

class Ticket(Base):
    __tablename__ = "Ticket"
    
    ticket_id : Mapped[int] = mapped_column()  


class TicketNotes(Base):
    pass      
