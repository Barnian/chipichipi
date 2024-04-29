from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from base_meta import Base


class Comment(Base):
    __tablename__ = "comment"

    # title_id = Column(ForeignKey("title.id"), primary_key=True)
    # user_id = Column(ForeignKey("user.id"), primary_key=True)
    usertitle_id = Column(ForeignKey("cmmnt.id"), primary_key=True)
    # title = relationship("Title", back_populates="titles")
    cmmnt = relationship("UserTitle", back_populates="cmmnts")

    # language_id = Column(ForeignKey("language.id"), primary_key=True)
    # user_id = Column(ForeignKey("user.id"), primary_key=True)
    #
    # language = relationship("Language", back_populates="users")
    # user = relationship("User", back_populates="languages")

