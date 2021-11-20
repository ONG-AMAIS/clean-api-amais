from ..helpers.connection import db


class User(db.Model):
    user_id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(232), nullable=False)
    user_type_id = db.Column(db.Integer(), nullable=False)
    person_id = db.Column(db.Integer(), nullable=False)
    created_at = db.Column(db.Date(), nullable=False)
    updated_at = db.Column(db.Date(), nullable=True)
    deleted_at = db.Column(db.Date(), nullable=True)
