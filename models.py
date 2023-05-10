"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""

from sqlalchemy import ForeignKey, Column, INTEGER, TEXT
from sqlalchemy.orm import relationship
from database import Base

# TODO: Complete your models

class User(Base):
    __tablename__ = "users"

    # Columns
    id = Column("id", INTEGER, primary_key=True, autoincrement=True)
    username = Column("username", TEXT)
    password = Column("password", TEXT)
    #points = Column("points", INTEGER) #Stretch Goal
    #followers and following Stretch Goal
    #posts = relationship("Post" back_populates="person")


class Post(Base):
    __tablename__ = "posts"
    # TODO: Complete the class

    #Columns
    id = Column("id", INTEGER, primary_key=True)
    description = Column("description", TEXT)
    likes = Column("likes", INTEGER)
    dislikes = Column("dislikes", INTEGER)
    #comments = Column("comments", type=comments)
    user_id = Column("user_id", TEXT, ForeignKey('users.id'))
    snack_id = Column("snack_id", TEXT, ForeignKey('snacks.id'))

class Snack(Base):
    __tablename__ = "snacks"

    #Columns
    id = Column("id", INTEGER, primary_key=True)
    name = Column("name", TEXT)
    rating = Column("rating", INTEGER)
    picture = Column("picture", TEXT)
    #posts = relationship("Post", back_populates="snacks")
    
    def __init__(self, name, rating, picture):
        self.name = name
        self.rating = rating
        self.picture = picture