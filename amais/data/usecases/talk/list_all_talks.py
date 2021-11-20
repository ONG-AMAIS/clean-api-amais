from amais.infra.db.talk.talk_repository import TalkRepository
from amais.utils.exceptions import Error


class ListAllTalks:
    @classmethod
    def list(self):
        talks = TalkRepository().get_all()
        if not talks:
            raise Error('NOT_FOUND')

        return talks
