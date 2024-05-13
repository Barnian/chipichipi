from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from .base_meta import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    date_of_registration = Column(Date, nullable=False)
    titles = relationship("UserTitle", back_populates="user")
    mail = Column(String, nullable=False)
    psw = Column(String, nullable=False)
    # answers = relationship("UserComment", back_populates="answer")

    # id = Column(Integer, primary_key=True, autoincrement=True)
    # full_name = Column(String, nullable=False)
    #
    # phones = relationship("Phone", back_populates="user")
    # languages = relationship("UserLanguage", back_populates="user")
    #
    # def __str__(selfr(id={self.id}, full_name='{self.full_name}')"
    #
