from ..helpers import db


class TalkSubscription(db.Model):
    talk_subscription_id = db.Column(db.Integer(), primary_key=True)
    talk_id = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    created_at = db.Column(db.Date(), nullable=False)
