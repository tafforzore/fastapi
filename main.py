from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from databases import Database
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Définir votre modèle de données
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
)

# Créer la base de données
metadata.create_all(bind=engine)

# Configurer la connexion à la base de données
database = Database(DATABASE_URL)

app = FastAPI()

# Définir une dépendance pour obtenir la session de la base de données
def get_db():
    db = None
    try:
        db = database
        yield db
    finally:
        db.close()

# Exemple de point de terminaison FastAPI utilisant la base de données
@app.get("/users/{user_id}")
async def read_user(user_id: int, db: Database = Depends(get_db)):
    query = users.select().where(users.c.id == user_id)
    user = await db.fetch_one(query)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
