from sqlalchemy.sql import func
from ..helpers.config import db
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

        return cls.__format_talk(talk)

    @ classmethod
    def get_all(cls):
        talk = Talk.query.all()
        if not talk:
            return None

        return cls.__format_talk(talk)

    @classmethod
    def __format_talk(cls, talk: Talk) -> dict:
        if isinstance(talk, list):
            return (({'id': item.talk_id, 'title': item.title,
                      'price': item.price, 'duration': item.duration,
                      'description': item.description, 'date': str(item.date),
                      'created_at': str(item.created_at)}) for item in talk)

        return {'id': talk.talk_id, 'title': talk.title,
                'title': talk.title, 'price': talk.price,
                'date': str(talk.date), 'duration': talk.duration,
                'description': talk.description, 'created_at': str(talk.created_at)}
