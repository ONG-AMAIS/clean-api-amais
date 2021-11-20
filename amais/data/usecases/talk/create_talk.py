from amais.infra.db.person.person_repository import PersonRepository
from amais.infra.db.talk.talk_repository import TalkRepository
from amais.infra.db.certificate.certificate_repository import CertificateRepository
from amais.main.configs.constants import UPLOAD_FOLDER
from amais.utils.exceptions import Error
from werkzeug.datastructures import FileStorage
from amais.domain.models.address import Addres
import secrets


class CreateTalk:

    @classmethod
    def create(cls, title: str, description: str, duration: int, presenter_document: str, price: str | None, date: str, file: FileStorage, address: Addres):

        person = PersonRepository().find_by_document(cpf=presenter_document)

        if not person:
            raise Error('PERSON_NOT_FOUND')

        extension = file.filename.split('.')[1]

        if extension != 'html':
            raise Error('EXTENSION_NOT_ALLOWED')

        file_name = secrets.token_hex(32)

        file_name_with_extension = "{file_name}.{extension}".format(
            file_name=file_name, extension=extension)

        file.save("{upload_folder}{file_name}".format(
            upload_folder=UPLOAD_FOLDER, file_name=file_name_with_extension))

        certificate = CertificateRepository().insert(file_name=file_name_with_extension)

        TalkRepository().insert(address=address, date=date, title=title,
                                description=description, duration=duration,
                                person_id=person['id'],
                                price=price, certificate_id=certificate['id'])
