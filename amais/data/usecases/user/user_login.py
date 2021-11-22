from amais.infra.db.user.user_repository import UserRepository
import hashlib

from amais.utils.exceptions import Error


class UserLogin:
    @classmethod
    def login(cls, login: str, password: str):
        decoded_string = password.encode('UTF-8')
        pass_hash = hashlib.sha256(decoded_string).hexdigest()
        user = UserRepository().login(login=login, password=pass_hash)

        if not user:
            raise Error('INCORRECT_CREDENTIALS')

        return user
