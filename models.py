from sqlalchemy import Column, Integer, String, MetaData, Table

metadata = MetaData()

# Définition du modèle de données
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
)
