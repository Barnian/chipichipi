from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from base_meta import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)

    phones = relationship("Phone", back_populates="user")
    languages = relationship("UserLanguage", back_populates="user")

    def __str__(self):
        return f"User(id={self.id}, full_name='{self.full_name}')"

