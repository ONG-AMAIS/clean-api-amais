# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, Float, Integer, String, TIMESTAMP, Table, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Addres(Base):
    __tablename__ = 'address'

    id_address = Column(Integer, primary_key=True)
    street = Column(String(45), nullable=False)
    district = Column(String(45), nullable=False)
    number = Column(String(10), nullable=False)
    complement = Column(String(10))
    id_city = Column(Integer, nullable=False, index=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class AutismLevel(Base):
    __tablename__ = 'autism_level'

    id_autism_level = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    description = Column(String(255))
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class City(Base):
    __tablename__ = 'city'

    id_city = Column(Integer, primary_key=True)
    id_state = Column(Integer, nullable=False, index=True)
    name = Column(String(45), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


t_consultation_document = Table(
    'consultation_document', metadata,
    Column('consultation_id_consultation', Integer, nullable=False, index=True),
    Column('document_id_document', Integer, nullable=False, index=True)
)


class Country(Base):
    __tablename__ = 'country'

    id_country = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    alpha_code = Column(String(3), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Day(Base):
    __tablename__ = 'days'

    id_day = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class DaysAvailability(Base):
    __tablename__ = 'days_availability'

    id_days_availability = Column(Integer, primary_key=True)
    id_day = Column(Integer, nullable=False, index=True)
    id_voluntary = Column(Integer, nullable=False, index=True)
    schedule = Column(String(45), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Document(Base):
    __tablename__ = 'document'

    id_document = Column(Integer, primary_key=True)
    url = Column(String(100), nullable=False, comment='Endereço do HTML do certificado')
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Patient(Base):
    __tablename__ = 'patient'

    id_patient = Column(Integer, primary_key=True)
    deficiency = Column(String(255), nullable=False)
    special_ability = Column(String(255))
    in_school = Column(String(100))
    do_therapy = Column(String(45))
    family_income = Column(String(45), nullable=False)
    id_address = Column(Integer, nullable=False, index=True)
    id_person = Column(Integer, nullable=False, index=True)
    id_autism_level = Column(Integer, nullable=False, index=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Person(Base):
    __tablename__ = 'person'

    id_person = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    cpf = Column(String(14), nullable=False)
    rg = Column(String(15))
    phone = Column(String(14), nullable=False)
    email = Column(String(45))
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class State(Base):
    __tablename__ = 'state'

    id_state = Column(Integer, primary_key=True)
    id_country = Column(Integer, nullable=False, index=True)
    name = Column(String(20), nullable=False)
    uf = Column(String(2), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Talk(Base):
    __tablename__ = 'talk'

    id_talk = Column(Integer, primary_key=True)
    type_talk = Column(String(1), nullable=False, comment='Fisica ou online')
    duration_talk = Column(Integer, nullable=False)
    talk_value = Column(Float(10, True), nullable=False, server_default=text("'0.00'"))
    id_certificate = Column(Integer, nullable=False, index=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TalkAddres(Base):
    __tablename__ = 'talk_address'

    id_talk_address = Column(Integer, primary_key=True)
    id_address = Column(Integer, nullable=False, index=True)
    id_talk = Column(Integer, nullable=False, index=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TalkTheme(Base):
    __tablename__ = 'talk_theme'

    id_talk_theme = Column(Integer, primary_key=True)
    id_theme = Column(Integer, nullable=False, index=True)
    id_talk = Column(Integer, nullable=False, index=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TalkVoluntary(Base):
    __tablename__ = 'talk_voluntary'

    id_talk_voluntary = Column(Integer, primary_key=True)
    id_voluntary = Column(Integer, nullable=False, index=True)
    id_talk = Column(Integer, nullable=False, index=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Theme(Base):
    __tablename__ = 'theme'

    id_theme = Column(Integer, primary_key=True)
    theme = Column(String(45), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Therapist(Base):
    __tablename__ = 'therapist'

    id_consultation = Column(Integer, primary_key=True)
    document = Column(String(45))
    voluntary = Column(CHAR(1), nullable=False)
    amount_paid = Column(DECIMAL(10, 0))
    specialization = Column(String(50), nullable=False)
    address_id_address = Column(Integer, nullable=False, index=True)
    user_id_user = Column(Integer, nullable=False, index=True)


class TherapistAttachment(Base):
    __tablename__ = 'therapist_attachment'

    id_therapist_attachment = Column(Integer, primary_key=True)
    therapist_id_consultation = Column(Integer, nullable=False, index=True)
    document_id_document = Column(Integer, nullable=False, index=True)


class User(Base):
    __tablename__ = 'user'

    id_user = Column(Integer, primary_key=True)
    login = Column(String(25), nullable=False)
    password = Column(String(232), nullable=False)


class Voluntary(Base):
    __tablename__ = 'voluntary'

    id_voluntary = Column(Integer, primary_key=True)
    id_person = Column(Integer, nullable=False, index=True)
    occupation = Column(String(255), nullable=False)
    url_document = Column(String(100), comment='Anexo de documento do voluntario com assinatura ')
    description_occupation = Column(Text)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))