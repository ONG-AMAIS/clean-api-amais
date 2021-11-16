from sqlalchemy.sql import func
from ..helpers.config import db
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
        result = Donation.query.all()
        return (({'donor': row.donor, 'value': row.value, 'description': row.description, }) for row in result)
