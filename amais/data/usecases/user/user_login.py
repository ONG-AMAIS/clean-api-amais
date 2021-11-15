from amais.infra.db.user.user_repository import UserRepository


class UserLogin:
    @classmethod
    def login(cls, login: str, password: str):
        result = UserRepository().login(login=login, password=password)
        print(result)
        return result != None
