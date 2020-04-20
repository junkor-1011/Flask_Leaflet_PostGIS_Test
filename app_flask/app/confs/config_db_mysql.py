"""Flask-SQLAlchemyにおけるdb接続用の設定ファイルi

- 参考
    - https://qiita.com/shirakiya/items/0114d51e9c189658002e
    - https://qiita.com/nsuhara/items/fa5998c0b2f4fcefbed4

"""

import os


class MySQL_DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{db_name}?client_encoding=utf8'.format(**{
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{db_port}/{db_name}?charset=utf8'.format(**{
        'user': os.getenv('DB_USER', 'test_user'),
        'password': os.getenv('DB_PASSWORD', 'password'),
        'host': os.getenv('DB_HOST', 'db_mysql'),
        'db_name': os.getenv('DB_DEFAULT', 'test_db'),
        'db_port': os.getenv('DB_PORT', '3306'),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = MySQL_DevelopmentConfig


