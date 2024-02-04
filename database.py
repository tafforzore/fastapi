from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from databases import Database

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Définition du modèle de données
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
)

# Création de la base de données
metadata.create_all(bind=engine)

# Configuration de la connexion à la base de données
database = Database(DATABASE_URL)
