"""おおよそDBのテーブルスキーマに対応

"""

import datetime

#from sqlalchemy.sql import text

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


class CoordsEvent(db.Model):

    __tablename__ = "coords_event"

    event_id = db.Column(db.String(255), primary_key=True)
    date = db.Column(db.Date, index=True, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    players_a = db.Column(db.JSON, nullable=True)
    players_b = db.Column(db.JSON, nullable=True)
    #arr_data = db.Column(db.ARRAY(db.String(255)), nullable=True)  # mysqlではコンパイルエラーが起きた
    date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    coords_detail_a = db.relationship("CoordsDetailA", backref=db.backref("coords_event"))
    coords_detail_b = db.relationship("CoordsDetailB", backref=db.backref("coords_event"))


class CoordsDetailA(db.Model):
    
    __tablename__ = "coords_detail_a"

    __table_args__ = (db.Index("ix_coords_detail_a_1", "event_id", "player", "latitude", "longitude", unique=False,), )

    event_id = db.Column('event_id', db.String(255),
        db.ForeignKey('coords_event.event_id',onupdate='CASCADE', ondelete='CASCADE'),
        primary_key=True,
    )
    #event_id = db.Column(db.String(255), primary_key=True, index=True)
    player = db.Column(db.String(255), primary_key=True)
    visit_order = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.String(255))
    site_type = db.Column(db.String(255))
    rec_type = db.Column(db.String(255))
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    val_a = db.Column(db.Float, nullable=True)
    ts_utc = db.Column(db.DateTime, nullable=False)
    ts_int = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)


class CoordsDetailB(db.Model):

    __tablename__ = "coords_detail_b"

    __table_args__ = (db.Index("ix_coords_detail_b_1", "event_id", "player", "latitude", "longitude", unique=False,), )

    event_id = db.Column('event_id', db.String(255),
        db.ForeignKey('coords_event.event_id',onupdate='CASCADE', ondelete='CASCADE'),
        primary_key=True,
    )
    #event_id = db.Column(db.String(255), primary_key=True, index=True)
    player = db.Column(db.String(255), primary_key=True)
    visit_order = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.String(255))
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    val_b = db.Column(db.Float, nullable=True)
    ts_utc = db.Column(db.DateTime, nullable=False)
    ts_int = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)



class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(sep=" "),
            "updated_at": self.updated_at.isoformat(sep=" "),
        }

    def get_users():
        #records = User.query.distinct(User.name)    # db.session.query(User).distinct(User.name)
        #records = db.session.query(User).distinct(User.name)
        records = db.session.query(User.name).distinct()
        users = [v.name for v in records]

        rec_count = User.query.count()

        #return users
        return {"users": users, "record_count": rec_count}

    def register_user(user):
        record = User(id=user['id'], name=user['name'])

        db.session.add(record)
        db.session.commit()

        return user

    def get_users_with_text(limit_num=2):
        """***

        - https://docs.sqlalchemy.org/en/13/orm/session_api.html#sqlalchemy.orm.session.Session.execute
        """
        #print(limit_num)   # for DEBUG
        from sqlalchemy.sql import text
        sql = text("SELECT DISTINCT name from users limit :limit")
        #records = db.session.execute(t, limit=limit_num)
        records = db.session.execute(sql, {"limit": limit_num})
        users = [v.name for v in records]

        return users


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



