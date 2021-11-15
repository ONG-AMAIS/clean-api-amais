from amais.infra.db.user.user_repository import UserRepository


class UpdateUser:
    @classmethod
    def update(self, id: int, login: str, password: str):
        userRepository = UserRepository()

        user = userRepository.update_by_id(
            id=id, login=login, password=password)

        return user != None
