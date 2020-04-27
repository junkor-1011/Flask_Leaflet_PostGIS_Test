"""Flask-SQLAlchemyにおけるdb接続用の設定ファイルi

- 参考
    - https://qiita.com/shirakiya/items/0114d51e9c189658002e
    - https://qiita.com/nsuhara/items/fa5998c0b2f4fcefbed4

"""

import os


class SQLite3_DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    #SQLALCHEMY_DATABASE_URI = 'sqlite:////app/db_sqlite3/data.sqlite3'   # TMP
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../../db_sqlite3/data.sqlite3'   # TMP
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True      # for Test


Config = SQLite3_DevelopmentConfig


