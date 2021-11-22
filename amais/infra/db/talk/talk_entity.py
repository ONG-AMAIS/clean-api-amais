from ..helpers.connection import db


class Talk(db.Model):
    talk_id = db.Column(db.Integer(), primary_key=True)
    duration = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.String(20), nullable=True)
    description = db.Column(db.String(20), nullable=True)
    title = db.Column(db.String(20), nullable=True)
    certificate_id = db.Column(db.Integer(), nullable=False)
    person_id = db.Column(db.Integer(), nullable=False)
    address = db.Column(db.JSON(), nullable=True)
    date = db.Column(db.Date(), nullable=False)
    created_at = db.Column(db.Date(), nullable=False)
    updated_at = db.Column(db.Date(), nullable=True)
    deleted_at = db.Column(db.Date(), nullable=True)
