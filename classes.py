# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, ForeignKey, Integer, String, Table, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class StAdministrator(Base):
    __tablename__ = 'st_administrator'

    ID = Column(BigInteger, primary_key=True)
    PASSWORD = Column(String(255))
    USERNAME = Column(String(255))


class StCar(Base):
    __tablename__ = 'st_car'

    ID = Column(BigInteger, primary_key=True)
    BRAND = Column(String(255))
    LASTUPDATED = Column(DateTime)
    NAME = Column(String(255))
    YEAROFFIRSTENTRY = Column(Integer)
    USER_ID = Column(ForeignKey(u'st_user.ID'), index=True)

    st_user = relationship(u'StUser')
    st_position = relationship(u'StPosition', secondary='st_car_st_position')


t_st_car_st_position = Table(
    'st_car_st_position', metadata,
    Column('Car_ID', ForeignKey(u'st_car.ID'), primary_key=True, nullable=False),
    Column('positions_ID', ForeignKey(u'st_position.ID'), primary_key=True, nullable=False, index=True)
)


class StPosition(Base):
    __tablename__ = 'st_position'

    ID = Column(BigInteger, primary_key=True)
    DTYPE = Column(String(31))
    LASTUPDATED = Column(DateTime)
    LATITUDE = Column(Float)
    LONGITUDE = Column(Float)


class StZone(StPosition):
    __tablename__ = 'st_zone'

    ID = Column(ForeignKey(u'st_position.ID'), primary_key=True)
    ENDTIME = Column(Time)
    RADIUS = Column(Integer)
    STARTTIME = Column(Time)
    CAR_ID = Column(ForeignKey(u'st_car.ID'), index=True)

    st_car = relationship(u'StCar')


class StUser(Base):
    __tablename__ = 'st_user'

    ID = Column(BigInteger, primary_key=True)
    CREDITCARD = Column(String(255))
    EMAIL = Column(String(255), unique=True)
    FIRSTNAME = Column(String(255))
    LASTNAME = Column(String(255))
    LASTUPDATED = Column(DateTime)
    PASSWORD = Column(String(255))
    PHONENUMBER = Column(String(255), unique=True)
    POSTALADDRESS = Column(String(255))
    USERNAME = Column(String(255), unique=True)

    st_position = relationship(u'StPosition', secondary='st_user_st_position')


t_st_user_st_position = Table(
    'st_user_st_position', metadata,
    Column('User_ID', ForeignKey(u'st_user.ID'), primary_key=True, nullable=False),
    Column('positions_ID', ForeignKey(u'st_position.ID'), primary_key=True, nullable=False, index=True)
)
