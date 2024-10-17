import os
import sys
import enum
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, UniqueConstraint, DateTime, func
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50))
    password = Column(String(100))
    join_date = Column(DateTime, server_default=func.now())



class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(200))
    gender = Column(String(50))
    eye_color = Column(String(50))
    hair_color = Column(String(50))
    height = Column(String(50))

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    terrain = Column(String(100))
    population = Column(Integer)
    climate = Column(String(50))


class Favorites(Base):
    __tablename__='favorites'

    id= Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    planet_id = Column(ForeignKey('planets.id'), nullable=True)
    character_id = Column(ForeignKey('characters.id'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
