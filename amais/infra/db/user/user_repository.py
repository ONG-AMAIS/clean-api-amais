from ..helper.config import db
from .user_entity import User


class UserRepository():
    @classmethod
    def insert(self, login, password):
        user = User(login=login, password=password)
        db.session.add(user)
        db.session.commit()

    @classmethod
    def get_all(self):
        result = User.query.all()

        return (({'id': row.user_id, 'login': row.login, 'password': row.password}) for row in result)
