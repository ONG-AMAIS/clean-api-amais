from ..helper.config import db


class User(db.Model):
    user_id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(232), nullable=False)
    created_at = db.Column(db.Date(), nullable=True)
    updated_at = db.Column(db.Date(), nullable=True)
    deleted_at = db.Column(db.Date(), nullable=True)
