from amais.infra.db.user.user_repository import UserRepository


class ListAllUsers:
    @classmethod
    def list(self):
        return UserRepository().get_all()
