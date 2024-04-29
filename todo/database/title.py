from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from base_meta import Base


class Title(Base):
    __tablename__ = "title"

    id = Column(Integer, primary_key=True, autoincrement=True)
    like = Column(Integer, nullable=False)
    dislike = Column(Integer, nullable=False)
    watched = Column(Integer, nullable=False)
    article_link = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    users = relationship("UserTitle", back_populates="user")
    comments = relationship("UserComment", back_populates="comment")
