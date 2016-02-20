# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Etudiant(Base):
    __tablename__ = 'etudiants'

    ID = Column(Integer, primary_key=True)
    Nom = Column(String(50), nullable=False)
    Prenom = Column(String(50), nullable=False)
    Email = Column(String(50), nullable=False)
    filier_id = Column(ForeignKey(u'filieres.ID'), nullable=False, index=True)

    filier = relationship(u'Filiere')


class Filiere(Base):
    __tablename__ = 'filieres'

    ID = Column(Integer, primary_key=True)
    Nom = Column(String(50), nullable=False)

    modules = relationship(u'Module', secondary='filieres_modules')


t_filieres_modules = Table(
    'filieres_modules', metadata,
    Column('id_filiere', ForeignKey(u'filieres.ID'), primary_key=True, nullable=False),
    Column('id_module', ForeignKey(u'modules.ID'), primary_key=True, nullable=False, index=True)
)


class Module(Base):
    __tablename__ = 'modules'

    ID = Column(Integer, primary_key=True)
    Nom = Column(String(50), nullable=False)
