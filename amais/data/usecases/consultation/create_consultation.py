from amais.infra.db.person.person_repository import PersonRepository
from amais.infra.db.patient.patient_repository import PatientRepository
from amais.infra.db.voluntary.voluntary_repository import VoluntaryRepository
from amais.infra.db.talk.talk_repository import TalkRepository
from amais.infra.db.certificate.certificate_repository import CertificateRepository
from amais.main.configs.constants import UPLOAD_FOLDER
from amais.utils.exceptions import Error
from werkzeug.datastructures import FileStorage
from amais.domain.models.address import Addres
import secrets


class CreateTalk:

    @classmethod
    def create(cls, patient_document: str, date: str, address: int, guidelines: str, voluntary_document: str, file: FileStorage):

        patient_person = PersonRepository().find_by_document(cpf=patient_document)
        voluntary_person = PersonRepository().find_by_document(cpf=voluntary_document)

        if not patient_person:
            raise Error('PATIENT_NOT_FOUND')

        if not voluntary_person:
            raise Error('VOLUNTARY_NOT_FOUND')

        patient = PatientRepository().find_by_person_id(
            person_id=patient_person['id']
        )

        voluntary = VoluntaryRepository().find_by_person_id(
            person_id=voluntary_person['id']
        )

        if not patient:
            raise Error('PATIENT_NOT_FOUND')

        if not voluntary:
            raise Error('VOLUNTARY_NOT_FOUND')

        [_, extension] = file.filename.split('.')

        if not extension in ('html', 'pdf', 'docx'):
            raise Error('EXTENSION_NOT_ALLOWED')

        str_hash = secrets.token_hex(32)

        file_name_with_extension = '{file_name}.{extension}'.format(
            file_name=str_hash,
            extension=extension
        )

        file_path = UPLOAD_FOLDER + file_name_with_extension
        file.save(file_path)

        # certificate = CertificateRepository().insert(file_name=file_name_with_extension)

        # TalkRepository().insert(address=address, date=date, title=title,
        #                         description=description, duration=duration,
        #                         person_id=person['id'],
        #                         price=price, certificate_id=certificate['id'])
