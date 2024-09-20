FROM python:latest

WORKDIR /app

# копируем библиотеки в папку app
COPY requirements.txt .


RUN pip install -r requirements.txt

# копируем код проекта в контейнер
COPY . .

EXPOSE 8000

# команда для запуска fastApi проекта
CMD ["uvicorn", "main:app", "--reload", "--port", "8000", "--host", "127.0.0.1"]

# команда для докер изображения
# docker build -t name_of_image .


# команда для запуска изображения терминал
# docker run -p 8000:8000 social_media_app

# docker run -p 8000:8000 --name назв контейнера назв изображения