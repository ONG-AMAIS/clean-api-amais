from sqlalchemy.sql import func

from amais.data.usecases import donation
from ..helpers import db, format
from .donation_entity import Donation


class DonationRepository():
    @classmethod
    def insert(cls, value: int, description: str, donor: str = None):
        donation = Donation(value=value, description=description,
                            donor=donor, created_at=func.now())
        db.session.add(donation)
        db.session.commit()

    @ classmethod
    def get_all(cls):
        donations = Donation.query.all()
        return format(cls.__donation_formatter, donations)

    @classmethod
    def __donation_formatter(cls, donation: Donation) -> dict:
        return dict({'id': donation.donation_id, 'donor': donation.donor, 'value': donation.value, 'description': donation.description, 'created_at': str(donation.created_at)})
