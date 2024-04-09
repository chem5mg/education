import os
import shutil
from zipfile import ZipFile

from fastapi.staticfiles import StaticFiles

from fastapi import APIRouter, UploadFile, File
from starlette.responses import FileResponse




router = APIRouter(tags=["API для хранения файлов"])

"""
Задание_5. API для хранения файлов

a.	Написать API для добавления(POST) "/upload_file" и скачивания (GET) "/download_file/{id}" файлов. 
В ответ на удачную загрузку файла должен приходить id для скачивания. 
b.	Добавить архивирование к post запросу, то есть файл должен сжиматься и сохраняться в ZIP формате.
с*.Добавить аннотации типов.
"""

d = {} #симуляция базы данных с id и путями к файлам
ID = 0
@router.post("/upload_file", description="Задание_5. API для хранения файлов")
async def upload_file(u_file: UploadFile = File(...)):
    """Описание."""
    global ID
    path = f'{u_file.filename}'

    with open(path, 'wb+') as buffer:
        shutil.copyfileobj(u_file.file, buffer)
        #shutil.make_archive('lala', 'zip', )

    #file_path = os.getcwd() + "/test"
    #shutil.make_archive(u_file.filename, 'zip', file_path)

    # create a ZipFile object
    zipObj = ZipFile(f'{u_file.filename}.zip', 'w')
    # Add multiple files to the zip
    zipObj.write(u_file.filename)
    # close the Zip File
    zipObj.close()

    d[ID] = u_file.filename
    ID += 1
    return ID
    # return file_id


@router.get("/download_file/{file_id}", description="Задание_5. API для хранения файлов")
async def download_file(file_id: int):
    """Описание."""

    # file = None
    return FileResponse(path=f'{d[file_id]}.zip', filename=f'{d[file_id]}.zip', media_type='application/octet-stream')
