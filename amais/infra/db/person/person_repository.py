from ..helpers.config import db
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
            return cls.__format_person(new_person)

        return cls.__format_person(current_person)

    @classmethod
    def __format_person(cls, person: Person) -> dict:
        return {'id': person.person_id, 'name': person.name, 'cpf': person.cpf,
                'rg': person.rg,  'phone': person.phone, 'email': person.email}
