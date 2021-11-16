from amais.infra.db.user.user_repository import UserRepository
from amais.infra.db.person.person_repository import PersonRepository
import hashlib


class CreateUser:
    UserType = {'name': str, 'cpf': str,
                'rg': str, 'login': str,  'password': str, 'phone': str, 'email': str}

    @classmethod
    def create(cls, name: str, cpf: str, phone: str, email: str, login: str, type_id: int, password: str, rg: str = None):
        pass_hash = hashlib.sha256(
            password.encode('UTF-8')).hexdigest()

        person = PersonRepository().find_or_create(
            cpf=cpf, name=name, phone=phone, email=email, rg=rg, )
        UserRepository().insert(password=pass_hash, user_type_id=type_id,
                                person_id=person.get('id'), login=login)
