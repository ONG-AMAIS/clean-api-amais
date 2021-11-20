from sqlalchemy.sql import func
from ..helpers import db, format
from .talk_entity import Talk


class TalkRepository():
    @classmethod
    def insert(cls,  description: str, title: str,  duration: int, person_id: int, price: str, date: str, address: dict,  certificate_id: str = 1):
        talk = Talk(description=description, duration=duration, title=title,
                    price=price, person_id=person_id, date=date,
                    certificate_id=certificate_id,
                    address=address, created_at=func.now())

        db.session.add(talk)
        db.session.commit()

    @ classmethod
    def find_by_person_id(cls, person_id: int):
        talk = Talk.query.filter_by(person_id=person_id).first()
        if not talk:
            return None

        return format(cls.__talk_formatter, talk)

    @ classmethod
    def get_all(cls):
        talks = Talk.query.all()
        if not talks:
            return None

        return format(cls.__talk_formatter, talks)

    @ classmethod
    def find_by_id(cls, talk_id: int):
        talk = Talk.query.filter_by(talk_id=talk_id).first()
        if not talk:
            return None

        return format(cls.__talk_formatter, talk)

    @classmethod
    def __talk_formatter(cls, item: Talk) -> dict:
        return dict({'id': item.talk_id, 'title': item.title,
                    'price': item.price, 'duration': item.duration,
                     'description': item.description, 'date': str(item.date),
                     'created_at': str(item.created_at)})
