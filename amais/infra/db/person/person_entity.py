from flask_sqlalchemy.model import Model
from ..helpers.config import db


class Person(db.Model):

    person_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    rg = db.Column(db.String(15))
    phone = db.Column(db.String(14), nullable=False)
    email = db.Column(db.String(45))
    created_at = db.Column(db.TIMESTAMP(), nullable=False,
                           server_default=db.text("CURRENT_TIMESTAMP"))
    updated_at = db.Column(db.TIMESTAMP(), nullable=False,
                           server_default=db.text(
        "CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
