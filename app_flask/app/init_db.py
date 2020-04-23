"""
debug時のテーブル初期化・生成用スクリプト

DBのデータは永続化しておく

Migrationなどまではやらないので、必要なら別途作る

"""

from database import db
from app import create_app
from flask_sqlalchemy import SQLAlchemy

# views
from models import views, CreateView

# create_all
if __name__ == '__main__':
    #db.init_app(create_app())
    db.create_all(app=create_app())
    #db.create_all()

    # create views
    #db.init_app(create_app())
    for view in views:
        #db.engine.execute(CreateView(view))
        SQLAlchemy(create_app()).engine.execute(CreateView(view))
