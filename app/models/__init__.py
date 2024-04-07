from typing import Union

from pydantic import BaseModel, ValidationError, field_validator


class ConverterRequest(BaseModel):
    number: Union[int, str]


class ConverterResponse(BaseModel):
    arabic: int
    roman: str


class User(BaseModel):
    name: str
    age: int
    adult: bool = None


class BigJson(BaseModel):
    """Использует модель User."""
    user: User
"""
    @field_validator('age')
    def age_val(self, v, values):
        if 0 > v > 100:
            raise ValueError('must be between 0 and 100')
        if values.adult > 18:
            values.adult = True
        else:
            values.adult = False
        return v.title(), values.adult"""




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
