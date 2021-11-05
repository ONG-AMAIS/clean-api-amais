from .exceptions import NotFoundException
from . import DatabaseSession


class MySqlStore:

    def update_object(self, entity, _id, params):

        with DatabaseSession() as session:
            data = session.query(entity). \
                filter(entity.id == _id). \
                first()

            if not data:
                # object not found
                raise NotFoundException()

            for k, v in params.items():
                if not hasattr(data, k):
                    raise ValueError("Entity {} has not property `{}`.".format(entity.__class__.__name__, k))
                setattr(data, k, v)

            session.commit()
            return data

    def normalize(self, o):
        # Implement here your desired logic to alter objects from data access layer to business logic (for example,
        # I like to replace SQL Alchemy entities with instances of classes that are abstracted from database)
        # This way, code in business logic and above is abstracted from specific database.
        if o is None:
            return None
        if isinstance(o, list):
            return [self.normalize(x) for x in o]
        return o
