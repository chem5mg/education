from fastapi import APIRouter

router = APIRouter(tags=["Стажировка"])

"""
Задание_8. Декоратор - счётчик запросов.

Напишите декоратор который будет считать кол-во запросов сделанных к приложению.
Оберните роут new_request() этим декоратором.
Подумать, как хранить переменную с кол-вом сделаных запросов.
"""


def counter(func):
    def wrapper():
        wrapper.count += 1
        writeToFile("app/count/file_counter.txt", wrapper.count)
        return func()

    wrapper.count = 0
    return wrapper


def writeToFile(path, count):
    with open(path, "w+") as file:
        file.write(str(count))


@router.get("/new_request", description="Задание_8. Декоратор - счётчик запросов.")
@counter
def new_request():
    return new_request.count