from ..helpers.config import db


class Donation(db.Model):
    donation_id = db.Column(db.Integer(), primary_key=True)
    donor = db.Column(db.String(255), nullable=True)
    value = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Date(), nullable=True)
