from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genre'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'director'

    name = Column(String(100), nullable=False)


class Movie(models.Base):
    __tablename__ = 'movie'

    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    trailer = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey("genre.id"))
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey("director.id"))
    director = relationship("Director")


class User(models.Base):
    __tablename__ = 'user'
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))
    # favorite_genre = Column(Integer, ForeignKey(Genre.id))
    # genre = relationship("Genre")