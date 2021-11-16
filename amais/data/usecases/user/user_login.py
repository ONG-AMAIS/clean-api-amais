from amais.infra.db.user.user_repository import UserRepository
import hashlib


class UserLogin:
    @classmethod
    def login(cls, login: str, password: str):
        pass_hash = hashlib.sha256(
            password.encode('UTF-8')).hexdigest()
        result = UserRepository().login(login=login, password=pass_hash)
        print(result)
        return result != None
