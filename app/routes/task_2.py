from typing import Annotated

from fastapi import APIRouter, Body, HTTPException, status

from app.core import convert_arabic_to_roman, convert_roman_to_arabic
from app.models import ConverterResponse


router = APIRouter(tags=["Стажировка"])

"""
Задание_2. Конвертер
    1. Реализовать функции convert_arabic_to_roman() и convert_roman_to_arabic() из пакета app.core
    2. Написать логику и проверки для вводимых данных. Учитывать, что если арабское число выходит за пределы 
    от 1 до 3999, то возвращать "не поддерживается"
    3. Запустить приложение и проверить результат через swagger
"""
@router.post("/converter", description="Задание_2. Конвертер")
async def convert_number(number: Annotated[int | str, Body()]) -> ConverterResponse:
    """
    Принимает арабское или римское число.
    Конвертирует его в римское или арабское соответственно.
    Возвращает первоначальное и полученное числа в виде json:
    {
        "arabic": 10,
        "roman": "X"
    }
    """

    if type(number) is int and 0 < number < 4000:
        roman = convert_arabic_to_roman(number)
        arabic = number
    elif type(number) is str:
        arabic = convert_roman_to_arabic(number.upper())
        roman = number
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Неверный тип данных, нужен int или str")
    converter_response = ConverterResponse(arabic = arabic, roman = roman)
    return converter_response
