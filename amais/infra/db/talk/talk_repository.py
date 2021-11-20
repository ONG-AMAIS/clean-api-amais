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
        return cls.__format_voluntary(talk)

    @ classmethod
    def get_all(cls):
        talk = Talk.query.all()
        return cls.__format_voluntary(talk)

    @classmethod
    def __format_voluntary(cls, talk: Talk) -> dict:
        if isinstance(talk, list):
            return (({'id': item.item_id, 'title': item.title, 'date': item.date, 'created_at': item.created_at}) for item in talk)

        return {'id': talk.talk_id, 'title': talk.title, 'date': talk.date, 'created_at': talk.created_at}
