from ..helpers.connection import db


class Voluntary(db.Model):
    voluntary_id = db.Column(db.Integer(), primary_key=True)
    occupation = db.Column(db.String(80), nullable=False)
    occupation_description = db.Column(db.String(255), nullable=True)
    document_url = db.Column(db.String(255), nullable=True)
    person_id = db.Column(db.Integer(), nullable=False)
    created_at = db.Column(db.Date(), nullable=False)
    updated_at = db.Column(db.Date(), nullable=True)
