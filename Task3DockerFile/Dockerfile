
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install django

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]