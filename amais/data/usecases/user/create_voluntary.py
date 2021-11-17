from amais.infra.db.user.user_repository import UserRepository
from amais.infra.db.person.person_repository import PersonRepository
from amais.infra.db.voluntary.voluntary_repository import VoluntaryRepository
import hashlib


class CreateVoluntary:

    @classmethod
    def create(cls, name: str, cpf: str, phone: str, email: str,
               login: str, password: str, occupation: str, document_url: str = None, rg: str = None, occupation_description: str = None):

        VOLUNTARY_ID = 2

        raw_bytes_password = password.encode('UTF-8')

        pass_hash = hashlib.sha256(raw_bytes_password).hexdigest()

        person = PersonRepository().find_or_create(
            cpf=cpf, name=name, phone=phone, email=email, rg=rg)

        voluntaryRepository = VoluntaryRepository()

        # voluntary = voluntaryRepository.find_by_person_id(
        #     person_id=person['id'])

        # if voluntary:
        #     return None

        voluntaryRepository.insert(occupation=occupation, document_url=document_url,
                                   person_id=person['id'], occupation_description=occupation_description)

        UserRepository().insert(password=pass_hash, user_type_id=VOLUNTARY_ID,
                                person_id=person.get('id'), login=login)
