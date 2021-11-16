from amais.infra.db.donation.donation_repository import DonationRepository


class CreateDonation:
    @classmethod
    def create(cls, value: str, description: str, donor: str = None):
        DonationRepository().insert(value=value, description=description, donor=donor)
