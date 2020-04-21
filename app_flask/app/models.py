"""おおよそDBのテーブルスキーマに対応

"""

import datetime

from database import db


class GeoPointTestA(db.Model):

    __tablename__ = 'geo_point_test_a'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    p_type = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    val_int = db.Column(db.Integer, nullable=True)
    val_float = db.Column(db.Float, nullable=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    ts_int = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    date = db.Column(db.Date, nullable=False)
    # todo method




class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_users(self):
        records = self.query.distinct(self.name)
        users = [v.name for v in records]
        return users

    def register_user(user):
        record = User(id=user['id'], name=user['name'])

        db.session.add(record)
        db.session.commit()

        return user



class Iris(db.Model):

    __tablename__ = 'iris'

    id = db.Column(db.Integer, primary_key=True)
    sepal_length = db.Column(db.Float, nullable=False)
    sepal_width = db.Column(db.Float, nullable=False)
    petal_length = db.Column(db.Float, nullable=False)
    petal_width = db.Column(db.Float, nullable=False)
    species = db.Column(db.String(255), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True, default=datetime.datetime.now, onupdate=datetime.datetime.now)


class Flights(db.Model):

    __tablename__ = 'flights'
    __table_args__ = (db.UniqueConstraint("year", "month", name="unique_year_month"), )
    # https://qiita.com/petitviolet/items/e03c67794c4e335b6706

    year = db.Column(db.Integer, primary_key=True, nullable=False)
    month = db.Column(db.String(255), primary_key=True, nullable=False)
    passengers = db.Column(db.Integer, nullable=False)


class Dots(db.Model):

    __tablename__ = 'dots'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    align = db.Column(db.String(255), nullable=False)
    choice = db.Column(db.String(255), nullable=False)
    time = db.Column(db.Integer, nullable=False)
    coherence = db.Column(db.Float, nullable=False)
    firing_rate = db.Column(db.Float, nullable=False)



