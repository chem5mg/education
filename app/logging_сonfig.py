import logging

# Создаем логгер
output_log = logging.getLogger("output")

# Устанавливаем уровень логирования
output_log.setLevel(logging.INFO)

# Создаем форматтер
formatter = logging.Formatter('[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - | %(execution_time_sec)s | %('
                              'http_method)s | %(url)s | %(status_code)s |')

# Создаем обработчик для записи в файл
file_handler = logging.FileHandler('loggs/output.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
output_log.addHandler(file_handler)
