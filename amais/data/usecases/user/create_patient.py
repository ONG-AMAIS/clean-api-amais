from amais.__old_model.entities import Addres
from amais.infra.db.user.user_repository import UserRepository
from amais.infra.db.patient.patient_repository import PatientRepository
from amais.infra.db.person.person_repository import PersonRepository
from amais.domain.models.address import Addres
import hashlib


class CreatePatient:

    @classmethod
    def create(cls, name: str, cpf: str, phone: str, email: str,
               login: str, password: str, deficiency: str,
               do_therapy: str, autism_level: int,
               family_income: str,
               address: Addres,
               rg: str | None, special_ability: str = None, school: str = None,):

        PATIENT_ID = 3

        raw_bytes_password = password.encode('UTF-8')

        pass_hash = hashlib.sha256(raw_bytes_password).hexdigest()

        person = PersonRepository().find_or_create(cpf=cpf, email=email,
                                                   name=name, phone=phone, rg=rg)

        PatientRepository().insert(autism_level_id=autism_level, person_id=person['id'],
                                   address=address, deficiency=deficiency,
                                   do_therapy=do_therapy, family_income=family_income,
                                   school=school, special_ability=special_ability)

        UserRepository().insert(password=pass_hash, user_type_id=PATIENT_ID,
                                person_id=person['id'], login=login)
