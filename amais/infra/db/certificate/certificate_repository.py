from sqlalchemy.sql import func
from ..helpers import db, format
from .certificate_entity import Certificate


class CertificateRepository():
    @classmethod
    def insert(cls,  file_name: str):
        certificate = Certificate(file_name=file_name, created_at=func.now())
        db.session.add(certificate)
        db.session.commit()

        return format(cls.__certificate_formatter, certificate)

    @ classmethod
    def find_by_id(cls, certificate_id: int):
        certificate = Certificate.query.filter_by(
            certificate_id=certificate_id).first()
        return format(cls.__certificate_formatter, certificate)

    @classmethod
    def __certificate_formatter(cls, certificate: Certificate) -> dict:
        return dict({'id': certificate.certificate_id, 'file_name': certificate.file_name, 'created_at': certificate.created_at})
