from amais.infra.db.donation.donation_repository import DonationRepository


class ListAllDonations:
    @classmethod
    def list(self):
        return DonationRepository().get_all()
