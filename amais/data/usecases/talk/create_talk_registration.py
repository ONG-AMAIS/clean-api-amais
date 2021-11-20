from amais.infra.db.talk.talk_repository import TalkRepository
from amais.infra.db.talk_subscription.talk_subscription_repository import TalkSubscriptionRepository
from amais.utils.exceptions import Error


class CreateTalkRegistration:

    @classmethod
    def create(cls, name: str, cpf: str, talk_id: int):

        talk = TalkRepository().find_by_id(talk_id)

        if not talk:
            raise Error('TALK_NOT_FOUND')

        talkSubscriptionRepository = TalkSubscriptionRepository()

        registration = talkSubscriptionRepository.find_by_document_and_talk_id(
            cpf=cpf, talk_id=talk_id)

        if registration:
            raise Error('REGISTER_ALREADY_EXISTS')

        talkSubscriptionRepository.insert(
            name=name, talk_id=talk['id'], cpf=cpf)
