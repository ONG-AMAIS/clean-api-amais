from .connection import db


def format(formater, data):
    if not data:
        return

    if isinstance(data, list):
        return list(map(formater, data))

    return formater(data)
