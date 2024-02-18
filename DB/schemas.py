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

class UserCreate(UserBase):
    nom : str 
    second_nom : str 
    prenom : str 
    second_prenom : str
    username : str
    numeros : int
    sexe : str
    password: str
    pays : str 
    ville :str
    quartier : str 
    adresse : str
    etats_compte : str
    date_creation : str
    date_connection : str
    uuid : str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True