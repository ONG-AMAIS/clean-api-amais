from ..helpers.config import db


class Patient(db.Model):
    patient_id = db.Column(db.Integer(), primary_key=True)
    deficiency = db.Column(db.String(255), nullable=False)
    special_ability = db.Column(db.String(255), nullable=True)
    school = db.Column(db.String(255), nullable=True)
    do_therapy = db.Column(db.String(45), nullable=True)
    family_income = db.Column(db.String(20), nullable=True)
    person_id = db.Column(db.Integer(), nullable=False)
    autism_level_id = db.Column(db.Integer(), nullable=False)
    address = db.Column(db.JSON(), nullable=False)
    created_at = db.Column(db.Date(), nullable=False)
    updated_at = db.Column(db.Date(), nullable=True)
