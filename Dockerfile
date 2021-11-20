FROM python:3.10.0-slim

WORKDIR /app

USER root

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT [ "python", "/app/app.py" ]