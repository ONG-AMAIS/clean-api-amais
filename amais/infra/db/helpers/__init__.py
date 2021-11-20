from .connection import db


def format(formater, data):
    if isinstance(data, list):
        return list(map(formater, data))

    return formater(data)
