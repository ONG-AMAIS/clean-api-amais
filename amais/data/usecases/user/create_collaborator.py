from amais.infra.db.user.user_repository import UserRepository
from amais.infra.db.person.person_repository import PersonRepository
import hashlib


class CreateCollaborator:

    @classmethod
    def create(cls, name: str, cpf: str, phone: str, email: str,
               login: str, password: str, rg: str = None):
        CONTRIBUITOR_ID = 1

        raw_bytes_password = password.encode('UTF-8')

        pass_hash = hashlib.sha256(raw_bytes_password).hexdigest()

        person = PersonRepository().find_or_create(
            cpf=cpf, name=name, phone=phone, email=email, rg=rg)

        UserRepository().insert(password=pass_hash, user_type_id=CONTRIBUITOR_ID,
                                person_id=person.get('id'), login=login)
