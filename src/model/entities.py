# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, Float, Integer, String, TIMESTAMP, Table, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TbAddres(Base):
    __tablename__ = 'tb_address'

    id_address = Column(Integer, primary_key=True)
    street = Column(String(45), nullable=False)
    district = Column(String(45), nullable=False)
    number = Column(String(10), nullable=False)
    complement = Column(String(10))
    id_city = Column(Integer, nullable=False, index=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TbAutismLevel(Base):
    __tablename__ = 'tb_autism_level'

    id_autism_level = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    description = Column(String(255))
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TbCity(Base):
    __tablename__ = 'tb_city'

    id_city = Column(Integer, primary_key=True)
    id_state = Column(Integer, nullable=False, index=True)
    name = Column(String(45), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


t_tb_consultation_document = Table(
    'tb_consultation_document', metadata,
    Column('tb_consultation_id_consultation', Integer, nullable=False, index=True),
    Column('document_id_document', Integer, nullable=False, index=True)
)


class TbCountry(Base):
    __tablename__ = 'tb_country'

    id_country = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    alpha_code = Column(String(3), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TbDay(Base):
    __tablename__ = 'tb_days'

    id_day = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TbDaysAvailability(Base):
    __tablename__ = 'tb_days_availability'

    id_days_availability = Column(Integer, primary_key=True)
    id_day = Column(Integer, nullable=False, index=True)
    id_voluntary = Column(Integer, nullable=False, index=True)
    schedule = Column(String(45), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TbDocument(Base):
    __tablename__ = 'tb_document'

    id_document = Column(Integer, primary_key=True)
    url = Column(String(100), nullable=False, comment='Endereço do HTML do certificado')
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TbPatient(Base):
    __tablename__ = 'tb_patient'

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


class TbPerson(Base):
    __tablename__ = 'tb_person'

    id_person = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    cpf = Column(String(14), nullable=False)
    rg = Column(String(15))
    phone = Column(String(14), nullable=False)
    email = Column(String(45))
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TbState(Base):
    __tablename__ = 'tb_state'

    id_state = Column(Integer, primary_key=True)
    id_country = Column(Integer, nullable=False, index=True)
    name = Column(String(20), nullable=False)
    uf = Column(String(2), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TbTalk(Base):
    __tablename__ = 'tb_talk'

    id_talk = Column(Integer, primary_key=True)
    type_talk = Column(String(1), nullable=False, comment='Fisica ou online')
    duration_talk = Column(Integer, nullable=False)
    talk_value = Column(Float(10, True), nullable=False, server_default=text("'0.00'"))
    id_certificate = Column(Integer, nullable=False, index=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TbTalkAddres(Base):
    __tablename__ = 'tb_talk_address'

    id_talk_address = Column(Integer, primary_key=True)
    id_address = Column(Integer, nullable=False, index=True)
    id_talk = Column(Integer, nullable=False, index=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TbTalkTheme(Base):
    __tablename__ = 'tb_talk_theme'

    id_talk_theme = Column(Integer, primary_key=True)
    id_theme = Column(Integer, nullable=False, index=True)
    id_talk = Column(Integer, nullable=False, index=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TbTalkVoluntary(Base):
    __tablename__ = 'tb_talk_voluntary'

    id_talk_voluntary = Column(Integer, primary_key=True)
    id_voluntary = Column(Integer, nullable=False, index=True)
    id_talk = Column(Integer, nullable=False, index=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TbTheme(Base):
    __tablename__ = 'tb_theme'

    id_theme = Column(Integer, primary_key=True)
    theme = Column(String(45), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TbTherapist(Base):
    __tablename__ = 'tb_therapist'

    id_consultation = Column(Integer, primary_key=True)
    document = Column(String(45))
    voluntary = Column(CHAR(1), nullable=False)
    amount_paid = Column(DECIMAL(10, 0))
    specialization = Column(String(50), nullable=False)
    tb_address_id_address = Column(Integer, nullable=False, index=True)
    tb_user_id_user = Column(Integer, nullable=False, index=True)


class TbUser(Base):
    __tablename__ = 'tb_user'

    id_user = Column(Integer, primary_key=True)
    login = Column(String(25), nullable=False)
    password = Column(String(232), nullable=False)


class TbVoluntary(Base):
    __tablename__ = 'tb_voluntary'

    id_voluntary = Column(Integer, primary_key=True)
    id_person = Column(Integer, nullable=False, index=True)
    occupation = Column(String(255), nullable=False)
    url_document = Column(String(100), comment='Anexo de documento do voluntario com assinatura ')
    description_occupation = Column(Text)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TherapistAttachment(Base):
    __tablename__ = 'therapist_attachment'

    id_therapist_attachment = Column(Integer, primary_key=True)
    tb_therapist_id_consultation = Column(Integer, nullable=False, index=True)
    document_id_document = Column(Integer, nullable=False, index=True)