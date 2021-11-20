from sqlalchemy.sql import func
from ..helpers.config import db
from .certificate_entity import Certificate


class CertificateRepository():
    @classmethod
    def insert(cls,  file_name: str):
        certificate = Certificate(file_name=file_name, created_at=func.now())
        db.session.add(certificate)
        db.session.commit()

        return cls.__format_certificate(certificate)

    @classmethod
    def __format_certificate(cls, certificate: Certificate) -> dict:
        return {'id': certificate.certificate_id, 'created_at': certificate.created_at}
