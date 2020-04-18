"""おおよそDBのテーブルスキーマに対応

"""

import datetime

from database import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)


class Iris(db.Model):

    __tablename__ = 'iris'

    id = db.Column(db.Integer, primary_key=True)
    sepal_length = db.Column(db.Float, nullable=False)
    sepal_width = db.Column(db.Float, nullable=False)
    petal_length = db.Column(db.Float, nullable=False)
    petal_width = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True, default=datetime.datetime.now, onupdate=datetime.datetime.now)


class Flights(db.Model):

    __tablename__ = 'flights'
    __table_args__ = (db.UniqueConstraint("year", "month", name="unique_year_month"), )
    # https://qiita.com/petitviolet/items/e03c67794c4e335b6706

    year = db.Column(db.Integer, primary_key=True, nullable=False)
    month = db.Column(db.String(255), primary_key=True, nullable=False)
    passengers = db.Column(db.Integer, nullable=False)




