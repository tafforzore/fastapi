from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    nom : str 
    second_nom : str 
    prenom : str 
    second_prenom : str | None = None
    username : str
    numeros : int
    sexe : str | None = None
    pays : str | None = None
    profession : str | None = None
    date_de_naissance : str | None = None
    lieu_de_naissance : str | None = None
    region : str | None = None
    quartier : str | None = None

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True