FROM python:3.10.0-slim

WORKDIR /app

USER root

COPY --chown=root:root ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY --chown=root:root . /app

ENTRYPOINT [ "python", "/app/app.py" ]