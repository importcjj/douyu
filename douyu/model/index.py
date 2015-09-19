# -*- coding:utf-8 -*-

from douyu.model import (
    Base,
    DBSession,
    Time
)
from sqlalchemy import (
    Column,
    Integer,
    String
)


class Index(Base, Time):
    __tablename__ = 'tb_index'
    __field__ = ['id']
    id = Column(Integer, primary_key=True)

    @classmethod
    def new(cls):
        index = cls()
        return index
