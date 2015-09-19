# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import (
    Column,
    DateTime,
    func
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 创建对象的基类
Base = declarative_base()


class Time(object):
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


# 创建数据库连接
engine = create_engine('mysql://{user}:{password}@{host}:{port}/{database}?charset=utf8'.format(
    user='root',
    password='jiaju',
    host='0.0.0.0',
    port='3306',
    database='douyuTv'),
    encoding="utf-8"
)
# 创建DBSession
DBSession = sessionmaker(bind=engine)


from .index import Index
from .card import RoomCard
