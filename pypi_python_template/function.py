from pydantic import BaseModel, EmailStr, validator
from typing_extensions import Annotated


class User(BaseModel):
    email: Annotated[EmailStr, validator("email", allow_reuse=True)]
    password: str
    name: str
    age: int
    is_admin: bool = False


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    age: int
    is_admin: bool = False


class UserUpdate(BaseModel):
    email: EmailStr
    name: str
    age: int
    is_admin: bool


class UserManagement:
    def __init__(self):  # type: ignore
        self.users = {}

    def create_user(self, user: UserCreate):  # type: ignore
        email = user.email
        if email in self.users:
            raise ValueError("User with that email already exists.")
        self.users[email] = user
        return user

    def update_user(self, email: str, user: UserUpdate):  # type: ignore
        if email not in self.users:
            raise ValueError("User with that email does not exist.")
        self.users[email] = user.email
        self.users[email] = user.name
        self.users[email] = user.age
        self.users[email] = user.is_admin
        return user

    def delete_user(self, email: str):  # type: ignore
        if email not in self.users:
            raise ValueError("User with that email does not exist.")
        del self.users[email]
