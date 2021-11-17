from sqlalchemy.sql import func
from ..helpers.config import db
from .patient_entity import Patient


class PatientRepository():
    @classmethod
    def insert(cls,  deficiency: str, special_ability: str, person_id: int, school: str, do_therapy: str, family_income: str, autism_level_id: int, address: dict):
        patient = Patient(deficiency=deficiency, special_ability=special_ability,
                          school=school, person_id=person_id, do_therapy=do_therapy,
                          family_income=family_income, autism_level_id=autism_level_id,
                          address=address, created_at=func.now())

        db.session.add(patient)
        db.session.commit()

    @ classmethod
    def find_by_person_id(cls, person_id: int):
        patient = Patient.query.filter_by(person_id=person_id).first()
        return cls.__format_voluntary(patient)

    @classmethod
    def __format_voluntary(cls, patient: Patient) -> dict:
        return {'id': patient.patient_id, 'person_id': patient.person_id}
