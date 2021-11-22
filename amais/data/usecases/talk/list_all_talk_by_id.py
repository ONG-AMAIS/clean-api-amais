from amais.infra.db.talk.talk_repository import TalkRepository
from amais.utils.exceptions import Error


class ListTalkById:
    @classmethod
    def list(self, talk_id: int):
        talk = TalkRepository().find_by_id(talk_id)
        if not talk:
            raise Error('NOT_FOUND')

        return talk
