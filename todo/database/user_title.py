from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from base_meta import Base


class UserTitle(Base):
    __tablename__ = "user_title"
    # id = Column(Integer, primary_key=True, autoincrement=True)
    title_id = Column(ForeignKey("title.id"), primary_key=True)
    user_id = Column(ForeignKey("user.id"), primary_key=True)

    title = relationship("Title", back_populates="titles")
    user = relationship("User", back_populates="users")
    cmmnts = Column(String)
    # language_id = Column(ForeignKey("language.id"), primary_key=True)
    # user_id = Column(ForeignKey("user.id"), primary_key=True)
    #
    # language = relationship("Language", back_populates="users")
    # user = relationship("User", back_populates="languages")

