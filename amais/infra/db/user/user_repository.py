from sqlalchemy.sql import func
from typing import List
from ..helpers import db, format
from .user_entity import User
from ..person.person_entity import Person
from ..user_type.user_type_entity import UserType


class UserRepository():
    @classmethod
    def insert(cls,  login: str, password: str, user_type_id: int, person_id: int) -> User:
        user = User(login=login, password=password,
                    user_type_id=user_type_id,
                    person_id=person_id,
                    created_at=func.now())

        db.session.add(user)
        db.session.commit()

        return format(cls.__user_formatter, user)

    @classmethod
    def login(cls, login: str, password: str) -> User:
        user = db.session.query(
            User.user_id,
            Person.name, Person.cpf,
            UserType.name,
            User.created_at
        ).select_from(User).join(
            Person,
            Person.person_id == User.person_id
        ).join(UserType,
               UserType.user_type_id == User.user_type_id
               ).filter(
            User.deleted_at == None,
            User.login == login,
            User.password == password
        ).first()

        return format(cls.user_formatter_with_person_rel, user)

    @ classmethod
    def get_all(cls) -> List[User]:
        users = db.session.query(
            User.user_id,
            Person.name, Person.cpf,
            UserType.name,
            User.created_at
        ).select_from(User).join(
            Person,
            Person.person_id == User.person_id
        ).join(UserType,
               UserType.user_type_id == User.user_type_id
               ).filter(User.deleted_at == None).all()

        return format(cls.user_formatter_with_person_rel, users)

    @ classmethod
    def find_by_id(cls, id: int) -> User:
        user = User.query.filter_by(user_id=id).first()
        return format(cls.__user_formatter, user)

    @ classmethod
    def update_by_id(cls, id: int, login: str, password: str) -> User:
        user = User.query.filter_by(user_id=id).first()

        if not user:
            return None

        user.login = login
        user.password = password
        user.updated_at = func.now()
        db.session.commit()

        return format(cls.__user_formatter, user)

    @ classmethod
    def delete_by_id(cls, id: int) -> User:
        user = User.query.filter_by(user_id=id).first()

        if not user:
            return None

        user.deleted_at = func.now()
        db.session.commit()
        return format(cls.__user_formatter, user)

    @ classmethod
    def user_formatter_with_person_rel(cls, user: User) -> dict:
        return dict({'id': user.user_id, 'name': user.name,
                     'document': user.cpf, 'type': user[3],
                     'created_at': str(user.created_at)})

    @ classmethod
    def __user_formatter(cls, user: User) -> dict:
        return dict({'id': user.user_id, 'login': user.login, 'created_at': str(user.created_at)})
