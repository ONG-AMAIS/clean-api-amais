from amais.infra.db.talk_subscription.talk_subscription_repository import TalkSubscriptionRepository
from amais.infra.db.talk.talk_repository import TalkRepository
from amais.infra.db.certificate.certificate_repository import CertificateRepository
from amais.utils.exceptions import Error


class GetTalkCertificate:

    @classmethod
    def get(cls, cpf: str, talk_id: int):
        talk = TalkRepository().find_by_id(talk_id)

        if not talk:
            raise Error('TALK_NOT_FOUND')

        talk_subscription = TalkSubscriptionRepository(
        ).find_by_document_and_talk_id(cpf=cpf, talk_id=talk_id)

        if not talk_subscription:
            raise Error('SUBSCRIPTION_NOT_FOUND')

        certificate = CertificateRepository(
        ).find_by_id(certificate_id=talk['certificate_id'])

        return {'talk': talk, 'entered': {
                'name': talk_subscription['name'],
                'cpf': talk_subscription['cpf']},
                'file_name': certificate['file_name']}
