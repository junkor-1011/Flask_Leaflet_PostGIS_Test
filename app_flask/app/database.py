"""FlaskアプリがSQLAlchemyを使えるための初期化

- 参考
    - https://qiita.com/shirakiya/items/0114d51e9c189658002e

"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)

