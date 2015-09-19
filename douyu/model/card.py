# -*- coding:utf-8 -*-
from sqlalchemy import (
    Column,
    Integer,
    String
)
from douyu.model import (
    Base,
    DBSession,
    Time
)


class RoomCard(Base, Time):

    __tablename__ = 'tb_card'
    __fields__ = ['crawlIndex', 'zbTitle', 'zbPlayer', 'zbViewer', 'zbType']

    id = Column(Integer, primary_key=True)
    crawlIndex = Column(Integer, default=0)
    zbTitle = Column(String(255), default='')
    zbPlayer = Column(String(255), default='')
    zbViewer = Column(Integer, default=0)
    zbType = Column(String(255), default='')

    @classmethod
    def new(cls, **kwargs):
        room_card = cls()
        for k, v in kwargs.iteritems():
            if k in cls.__fields__:
                setattr(room_card, k, v)
        return room_card
