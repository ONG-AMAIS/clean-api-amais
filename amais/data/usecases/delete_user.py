# pylint: disable=too-few-public-methods
from amais.infra.db.user.user_repository import UserRepository


class DeleteUser:
    @classmethod
    def delete(self, user_id: int):
        userRepository = UserRepository()
        user = userRepository.delete_by_id(id=user_id)
        return user != None
