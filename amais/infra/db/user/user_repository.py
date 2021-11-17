from typing import Dict
from sqlalchemy.sql import func
from ..helpers.config import db
from .user_entity import User
from ..person.person_entity import Person
from ..user_type.user_type_entity import UserType


class UserRepository():
    @classmethod
    def insert(cls,  login: str, password: str, user_type_id: int, person_id: int):
        user = User(login=login, password=password, user_type_id=user_type_id,
                    person_id=person_id, created_at=func.now())
        db.session.add(user)
        db.session.commit()

    @classmethod
    def login(cls, login: str, password: str):
        result = User.query.filter_by(
            login=login, password=password, deleted_at=None).first()

        if not result:
            return None

        return result

    @ classmethod
    def get_all(cls):
        result = db.session.query(Person.name, Person.cpf, UserType.name, User.created_at).select_from(
            User).join(Person, Person.person_id == User.person_id).join(UserType, UserType.user_type_id == User.user_type_id).all()

        return cls.__format_generic_user(result)

    @ classmethod
    def find_by_id(cls, id: int):
        result = User.query.filter_by(user_id=id).first()
        return cls.__format_user(result)

    @ classmethod
    def update_by_id(cls, id: int, login: str, password: str):
        result = User.query.filter_by(user_id=id).first()

        if not result:
            return None

        result.login = login
        result.password = password
        result.updated_at = func.now()

        db.session.commit()

        return cls.__format_user(result)

    @ classmethod
    def delete_by_id(cls, id: int):
        result = User.query.filter_by(user_id=id).first()

        if not result:
            return None

        result.deleted_at = func.now()

        db.session.commit()

    @ classmethod
    def __format_generic_user(cls, user: User) -> dict:

        if isinstance(user, list):
            return (({'name': item.name, 'document': item.cpf,
                      'type': item[2], 'created_at': str(item.created_at)}) for item in user)

        return {'name': user.name, 'document': user.cpf, 'type': user[2], 'created_at': str(user.created_at)}

    @ classmethod
    def __format_user(cls, user: User) -> dict:
        if isinstance(user, list):
            return (({'id': item.user_id, 'login': item.login}) for item in user)

        return {'id': user.user_id, 'login': user.login}
