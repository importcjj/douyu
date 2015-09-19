# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import (
    Column,
    DateTime,
    func
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

try:
    from douyu.myconf import MYSQL
except ImportError:
    print "ff"
    MYSQL = {
        'user': 'username',
        'password': 'password',
        'host': 'localhost',
        'port': '3306',
        'database': 'douyu'
    }


# 创建对象的基类
Base = declarative_base()


class Time(object):
    created_at = Column(DateTime, default=func.now())


# 创建数据库连接
engine = create_engine(
    'mysql://{user}:{password}@{host}:{port}/{database}?charset=utf8'.format(
        **MYSQL),
    encoding="utf-8"
)
# 创建DBSession
DBSession = sessionmaker(bind=engine)


from .index import Index
from .card import RoomCard
