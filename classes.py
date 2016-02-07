# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Mark(Base):
    __tablename__ = 'marks'

    ID = Column(BigInteger, primary_key=True)
    COURSENAME = Column(String(255))
    MARKVALUE = Column(Float)
    STUDENT_ID = Column(ForeignKey(u'students.ID'), index=True)

    student = relationship(u'Student')


class Student(Base):
    __tablename__ = 'students'

    ID = Column(BigInteger, primary_key=True)
    CREATIONDATE = Column(DateTime)
    NAME = Column(String(255))
