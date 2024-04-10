import time
from contextvars import ContextVar

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from app.logging_сonfig import output_log

client_host: ContextVar[str | None] = ContextVar("client_host", default=None)


class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        """Load request ID from headers if present. Generate one otherwise."""

        start_time = time.time()  # Засекаем время начала выполнения запроса
        client_host.set(request.client.host)
        # output_log.info(f"Accepted request {request.method} {request.url}")

        response = await call_next(request)

        # Засекаем время окончания выполнения запроса
        end_time = time.time()
        execution_time_sec = round(end_time - start_time, 2)

        # Формируем данные для логирования
        log_data = {
            "execution_time_sec": execution_time_sec,
            "http_method": request.method,
            "url": request.url,
            "status_code": response.status_code,
        }

        # Логируем данные
        output_log.info("", extra=log_data)
        # В случае ошибки при запросе, возвращать код 500
        if response.status_code == 500:
            response = Response("Internal Server Error", status_code=500)
        return response


"""
Задание_7. Логирование в FastAPI с использованием middleware.

Написать конфигурационный файл для логгера "output"
Формат выводимых логов:
[CURRENT_DATETIME] {file: line} LOG_LEVEL - | EXECUTION_TIME_SEC | HTTP_METHOD | URL | STATUS_CODE |
[2023-12-15 00:00:00] {example:62} INFO | 12 | GET | http://localhost/example | 200 |


Дописать класс CustomMiddleware.
Добавить middleware в приложение (app).
"""