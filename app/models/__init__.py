from typing import Union, Annotated

from fastapi import Body
from pydantic import BaseModel, ValidationError, field_validator
from pydantic.v1 import validator


class ConverterRequest(BaseModel):
    number: Union[int, str]


class ConverterResponse(BaseModel):
    arabic: int
    roman: str


class User(BaseModel):
    name: str
    age:  int
    adult: bool = None
    massage: str = None

class BigJson(BaseModel):
    """Использует модель User."""
    user: User
    @field_validator('user')
    def name_must_not_contain_space(cls, v):
        if ' ' in v.name:
            raise ValueError('не должно содержать пробелов')
        return v
    @field_validator('user')
    def name_must_contain_space(cls, v):
        if not 0 < v.age < 100:
            raise ValueError('не может быть меньше 0 и больше 100')
        if v.age > 18:
            v.adult = True
        else:
            v.adult = False
        return v

# class UserRequest(BaseModel):
#     name: str
#     message: str
#
#
# class User(BaseModel):
#     name: str
#     age: str
#     is_adult: bool
#     message: str = None
#
#
# class UserResponse(BaseModel):
#     pass
