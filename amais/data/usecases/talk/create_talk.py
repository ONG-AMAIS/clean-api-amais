from amais.infra.db.person.person_repository import PersonRepository
from amais.infra.db.talk.talk_repository import TalkRepository
from amais.main.configs.constants import UPLOAD_FOLDER
from amais.utils.exceptions import Error
from werkzeug.datastructures import FileStorage


class CreateTalk:

    Addres = {'street': str, 'district': str, 'number': str,
              'complement': str | None, 'city': str, 'state': str}

    @classmethod
    def create(cls, title: str, description: str, duration: int, presenter_document: str, price: str | None, date: str, file: FileStorage, address: Addres):

        person = PersonRepository().find_by_document(cpf=presenter_document)

        if not person:
            raise Error('PERSON_NOT_FOUND')

        file.save("{upload_folder}{file_name}".format(
            upload_folder=UPLOAD_FOLDER, file_name=file.filename))

        TalkRepository().insert(address=address, date=date, title=title,
                                description=description, duration=duration,
                                person_id=person['id'],
                                price=price, certificate_id=1)
