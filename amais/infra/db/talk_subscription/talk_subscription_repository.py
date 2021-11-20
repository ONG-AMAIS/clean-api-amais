from sqlalchemy.sql import func
from ..helpers import db, format
from .talk_subscription_entity import TalkSubscription


class TalkSubscriptionRepository():
    @classmethod
    def insert(cls,  name: str, cpf: str, talk_id: int):
        talk_subscription = TalkSubscription(name=name, cpf=cpf,
                                             talk_id=talk_id, created_at=func.now())

        db.session.add(talk_subscription)
        db.session.commit()

    @ classmethod
    def find_by_document(cls, cpf: str):
        talk = TalkSubscription.query.filter_by(cpf=cpf).first()
        return format(cls.__talk_formatter, talk)

    @ classmethod
    def get_all(cls):
        talk_subscription = TalkSubscription.query.all()
        return format(cls.__talk_formatter, talk_subscription)

    @ classmethod
    def find_by_id(cls, talk_subscription_id: int):
        talk_subscription = TalkSubscription.query.filter_by(
            talk_subscription_id=talk_subscription_id).first()
        return format(cls.__talk_formatter, talk_subscription)

    @classmethod
    def __talk_formatter(cls, item: TalkSubscription) -> dict:
        return dict({'id': item.talk_subscription_id, 'name': item.name,
                    'cpf': item.cpf, 'created_at': str(item.created_at)})
