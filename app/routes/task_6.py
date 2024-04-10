import time
from typing import Annotated

from fastapi import APIRouter, Body, HTTPException, status
from requests import HTTPError

from app.core import DataGenerator, YAMLWriter, CSVWriter, JSONWriter

router = APIRouter(tags=["API для хранения файлов"])

"""
Задание_6. 

Изучите следущие классы в модуле app.core: BaseWriter, DataGenerator

API должно принимать json, по типу:
{
    "file_type": "json",  # или "csv", "yaml"
    "matrix_size": int    # число от 4 до 15
}
В ответ на удачную генерацию файла должен приходить id для скачивания.

Добавьте реализацию методов класса DataGenerator.
Добавьте аннотации типов и (если требуется) модели в модуль app.models.

(Подумать, как переисползовать код из задания 5)
"""
@router.post("/generate_file", description="Задание_6. Конвертер")
async def generate_file(file_type: Annotated[str, Body()], matrix_size: Annotated[int, Body()]) -> int:
    """Описание."""

    if not 4 <= matrix_size < 15:
        raise HTTPError(status_code=400, detail="Неверный размер матрицы")

    path = f'test_task_6/{time.strftime("%Y%m%d-%H%M%S")}.{file_type}'

    data = DataGenerator()
    data.generate(matrix_size)
    match file_type.lower():
        case "json":
            json_writer = JSONWriter()
            data.to_file(path, json_writer.write(data.data))
        case "csv":
            csv_writer = CSVWriter()
            data.to_file(path, csv_writer.write(data.data))
        case "yaml":
            yaml_writer = YAMLWriter()
            data.to_file(path, yaml_writer.write(data.data))
        case _:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Укажите формат json, csv или yaml")


    file_id: int = data.file_id

    return file_id