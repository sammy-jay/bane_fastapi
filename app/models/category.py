from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

from app.models.post import post_category_association

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, default="")
    
    posts = relationship("Post", secondary=post_category_association, back_populates="categories")

