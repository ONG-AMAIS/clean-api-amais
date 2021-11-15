from amais.infra.db.user.user_repository import UserRepository


class CreateUser:
    @classmethod
    def create(self, login: str, password: str):
        user_repository = UserRepository()

        user_repository.insert(
            login=login, password=password,)
