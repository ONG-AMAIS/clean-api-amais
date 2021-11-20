from sqlalchemy.sql import func
from ..helpers import db, format
from .user_entity import User
from ..person.person_entity import Person
from ..user_type.user_type_entity import UserType


class UserRepository():
    @classmethod
    def insert(cls,  login: str, password: str, user_type_id: int, person_id: int):
        user = User(login=login, password=password,
                    user_type_id=user_type_id,
                    person_id=person_id,
                    created_at=func.now())

        db.session.add(user)
        db.session.commit()

    @classmethod
    def login(cls, login: str, password: str):
        user = User.query.filter_by(
            login=login,
            password=password,
            deleted_at=None
        ).first()

        return format(cls.__user_formatter, user)

    @ classmethod
    def get_all(cls):
        users = db.session.query(
            Person.name, Person.cpf,
            UserType.name,
            User.created_at
        ).select_from(User).join(
            Person,
            Person.person_id == User.person_id
        ).join(UserType,
               UserType.user_type_id == User.user_type_id
               ).all()

        return format(cls.__generic_user_formatter, users)

    @ classmethod
    def find_by_id(cls, id: int):
        user = User.query.filter_by(user_id=id).first()
        return format(cls.__user_formatter, user)

    @ classmethod
    def update_by_id(cls, id: int, login: str, password: str):
        user = User.query.filter_by(user_id=id).first()

        if not user:
            return None

        user.login = login
        user.password = password
        user.updated_at = func.now()
        db.session.commit()

        return format(cls.__user_formatter, user)

    @ classmethod
    def delete_by_id(cls, id: int):
        user = User.query.filter_by(user_id=id).first()

        if not user:
            return None

        user.deleted_at = func.now()
        db.session.commit()

    @ classmethod
    def __generic_user_formatter(cls, user: User) -> dict:
        return dict({'name': user.name, 'document': user.cpf, 'type': user[2], 'created_at': str(user.created_at)})

    @ classmethod
    def __user_formatter(cls, user: User) -> dict:
        return dict({'id': user.user_id, 'login': user.login})
