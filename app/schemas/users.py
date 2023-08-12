from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    name: str

class UserCreate(UserBase):
    password: str

class User(BaseModel):
    id: int

    class Config:
        from_attributes = True