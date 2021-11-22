from ..helpers.connection import db


class UserType(db.Model):
    user_type_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.Date(), nullable=False)
