from ..helpers.config import db


class Certificate(db.Model):
    certificate_id = db.Column(db.Integer(), primary_key=True)
    file_name = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.Date(), nullable=False)
