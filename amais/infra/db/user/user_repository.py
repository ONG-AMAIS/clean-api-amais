from typing import Dict
from sqlalchemy.sql import func
from ..helpers.config import db
from .user_entity import User


class UserRepository():
    @classmethod
    def insert(cls, login, password):
        user = User(login=login, password=password, created_at=func.now())
        db.session.add(user)
        db.session.commit()

    @classmethod
    def login(cls, login: str, password: str):
        result = User.query.filter_by(login=login, password=password).first()

        if not result:
            return None

        return result

    @ classmethod
    def get_all(cls):
        result = User.query.all()

        return (({'id': row.user_id, 'login': row.login, 'password': row.password}) for row in result)

    @ classmethod
    def find_by_id(cls, id: int):
        row = User.query.filter_by(user_id=id).first()
        return {'id': row.user_id, 'login': row.login, 'password': row.password}

    @ classmethod
    def update_by_id(cls, id: int, login: str, password: str):
        row = User.query.filter_by(user_id=id).first()

        if not row:
            return None

        row.login = login
        row.password = password
        row.updated_at = func.now()

        db.session.commit()

        return {'id': row.user_id, 'login': row.login, 'password': row.password}

    @ classmethod
    def delete_by_id(cls, id: int):
        row = User.query.filter_by(user_id=id).first()

        if not row:
            return None

        row.deleted_at = func.now()

        db.session.commit()
