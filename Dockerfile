# Используйте официальный образ Python
FROM python:3.9-slim

# Установите рабочую директорию в контейнере
WORKDIR /app

# Копируйте файлы приложения в контейнер
COPY . .

# Установите необходимые пакеты с помощью pip
RUN pip install --no-cache-dir Flask openai python-dotenv

# Задайте команду для запуска вашего приложения
CMD ["python", "input_chat_pre_final.py"]