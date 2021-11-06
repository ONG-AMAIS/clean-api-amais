from src.model.entities import Person
from src.config.store import MySqlStore
from src.config.store import DatabaseSession

class PersonRepository(MySqlStore):
    def insert(self,name,cpf,rg,phone,email):
        entity = Person

        instance = entity(name = name, cpf = cpf, rg = rg, phone = phone, email = email)
        
        with DatabaseSession() as session:
            session.add(instance)
            session.flush()
            session.commit()
            return self.normalize(instance)

    def get_person(self, id_person):
        with DatabaseSession() as session:
            data = session.query(Person).filter(Person.id_person == id_person).\
                   all()
            person = self.normalize(data)

        return person