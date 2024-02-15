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
    password: str
    nom : str 
    second_nom : str 
    prenom : str 
    second_prenom : str 
    username : str
    numeros : int
    sexe : str
    pays : str 
    region : str 
    quartier : str 
    type_msg_send : str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True