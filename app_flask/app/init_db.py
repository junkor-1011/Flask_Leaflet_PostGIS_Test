"""
debug時のテーブル初期化・生成用スクリプト

DBのデータは永続化しておく

Migrationなどまではやらないので、必要なら別途作る

"""

from database import db
from app import create_app

# create_all
if __name__ == '__main__':
    db.create_all(app=create_app())

 
