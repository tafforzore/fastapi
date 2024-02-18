from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
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
    ville = Column(String)
    quartier = Column(String)
    adresse = Column(String)

    #verifier si le compte de utilisateur est actifs ou bloquer
    etats_compte = Column(Boolean, default=True)

    #verifier si un user est en ligne 
    is_active = Column(Boolean, default=False)
    date_creation = Column(DateTime, default=datetime.now)
    date_connection = Column(DateTime, default=datetime.now)
    
    ##uid de utilisateur
    uuid = Column(String, default=lambda: str(uuid.uuid4()))



 
# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")