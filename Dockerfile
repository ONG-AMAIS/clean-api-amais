FROM python:3.10.0-slim

WORKDIR /app

USER app

COPY --chown=app:app ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY --chown=app:app . /app

ENTRYPOINT [ "python", "/app/app.py" ]