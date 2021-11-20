from sqlalchemy.sql import func
from ..helpers import db, format
from .voluntary_entity import Voluntary


class VoluntaryRepository():
    @classmethod
    def insert(cls,  occupation: str, occupation_description: str, person_id: int, document_url: str):
        voluntary = Voluntary(occupation=occupation,
                              occupation_description=occupation_description,
                              document_url=document_url,
                              person_id=person_id,
                              created_at=func.now())

        db.session.add(voluntary)
        db.session.commit()

    @ classmethod
    def find_by_person_id(cls, person_id: int):
        voluntary = Voluntary.query.filter_by(person_id=person_id).first()
        return format(cls.__voluntary_formatter, voluntary)

    @classmethod
    def __voluntary_formatter(cls, voluntary: Voluntary) -> dict:
        return dict({'id': voluntary.voluntary_id,
                     'occupation': voluntary.occupation,
                     'occupation_description': voluntary.occupation_description,
                     'document_url': voluntary.document_url,
                     'person_id': voluntary.person_id})
