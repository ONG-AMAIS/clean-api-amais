from ..helpers import db, format
from .person_entity import Person


class PersonRepository():
    @classmethod
    def find_or_create(cls, name: str, cpf: str, phone: str, email: str, rg: str = None):
        current_person = Person.query.filter_by(cpf=cpf).first()
        if not current_person:
            new_person = Person(name=name, cpf=cpf, rg=rg,
                                phone=phone, email=email)

            db.session.add(new_person)
            db.session.commit()
            return format(cls.__person_formatter, new_person)

        return format(cls.__person_formatter, current_person)

    @classmethod
    def find_by_document(cls, cpf: str):
        person = Person.query.filter_by(cpf=cpf).first()
        return format(cls.__person_formatter, person)

    @classmethod
    def __person_formatter(cls, person: Person) -> dict:
        return dict({'id': person.person_id, 'name': person.name,
                     'cpf': person.cpf, 'rg': person.rg,
                     'phone': person.phone, 'email': person.email})
