from pydantic import BaseModel


class UserLoginForm(BaseModel):
    email: str
    password: str


class UserCreateForm(BaseModel):
    email: str
    password: str
    first_name: str | None = None
    last_name: str | None = None
    nick_name: str | None = None
