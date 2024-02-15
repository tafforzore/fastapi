from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "Utilisateurs"

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    second_nom = Column(String)
    prenom = Column(String)
    second_prenom = Column(String)
    username = Column(String)
    numeros = Column(Integer)
    sexe = Column(String)
    email = Column(String)
    password = Column(String)
    pays = Column(String)
    quartier = Column(String)
    is_active = Column(Boolean, default=True)


 
# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")