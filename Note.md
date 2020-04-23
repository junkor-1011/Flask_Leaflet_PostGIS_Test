Note
======



### snipets

#### `curl` with authentication & ssl (insecure)

- https://qiita.com/greymd/items/68b0c40044a88171235a
- https://hacknote.jp/archives/25380/
- https://qiita.com/libra_lt/items/8102e9b10a17f2f7fb3b
- https://qiita.com/sensuikan1973/items/b2085a9cdc6d1e97e8f8
- https://qiita.com/ktooi/items/958bab82b828b389969a
- https://qiita.com/sukakako/items/9273fa05948af43ab39d

```Bash
curl -k -u user:password -H 'Content-Type:application/json' -XPOST -d '{"id": "3", "name": "Casaline"}' https://127.0.0.1:8443/models_test/create_user
```

#### `pandas` with `SQLAlchemy`

```Python
# import 
from sqlalchemy import create_engine
import pandas as pd

# create engine
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}:{db_port}/{db_name}?client_encoding=utf8'.format(**{
    'user': 'test_user',
    'password': 'password',
    'host': '172.19.0.1',
    'db_name': 'test_db',
    'db_port': '15432',
})
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# データを簡単にReadするだけならsessionを作らなくても良い
result = engine.execute("select * from iris limit 10")
for row in result:
    print(row)

# pandas

# tableの中身を全部取得する場合は以下が楽
pd.read_sql_table("iris", engine)

# SQL文を投げることも出来る(カラム名も正しく取得される)
# プレースホルダー、バインドなど厳密な安全性を考えなければ、簡便な値取得方法に使える
pd.read_sql_query("select * from dots limit 100", con=engine, index_col='id')

# データを挿入したりする場合は別途確認

```

--------------

### Links

#### SQLAlchemy

- documentation
    - https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.SQLAlchemy

- 一般的な使い方
    - https://qiita.com/tomo0/items/a762b1bc0f192a55eae8
    - https://qiita.com/tosizo/items/86d3c60a4bb70eb1656e
    - https://qiita.com/mink0212/items/d7f31f6e2903c5f0b837
    - https://www.slideshare.net/YasushiMasuda/playsqlalchemy-sqlalchemy

- 生のSQL文を使う
    - https://www.sukerou.com/2019/04/sqlalchemysqlsql.html
    - https://www.m3tech.blog/entry/sqlalchemy-tutorial1
    - https://www.python.ambitious-engineer.com/archives/1471

- `pandas`
    - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html#pandas.read_sql

##### Flask-SQLAlchemy

- General
    - https://qiita.com/msrks/items/673c083ca91f000d3ed1
    - https://qiita.com/shirakiya/items/0114d51e9c189658002e
        - 全般的な使い方
        - Migrationなども便利そう（ユースケース次第で検討）
    - https://swallow-incubate.com/archives/blog/20190909
        - `models.py`の各クラスの中で、各テーブルを典型的な操作を記述するメソッドが書ける
    - https://www.atmarkit.co.jp/ait/articles/1808/07/news029.html
        - `CRUD`ぽく
    - https://www.tcom242242.net/entry/2020/01/04/flask-sqlalchemy%E3%81%AE%E5%9F%BA%E6%9C%AC%E7%9A%84%E3%81%AA%E4%BD%BF%E3%81%84%E6%96%B9%E3%80%82mysql%E3%82%92%E4%BD%BF%E3%81%84%E3%81%BE%E3%81%99/
        - 簡単な使い方
    - https://study-flask.readthedocs.io/ja/latest/flask_sqlalchemy.html
    - https://akatak.hatenadiary.jp/entry/2019/07/06/114317
    - https://mycodingjp.blogspot.com/2019/03/flask-sqlalchemy.html


##### SQLAlchemy-Views

- viewを実テーブルのモデルのように扱うには工夫が必要な様子
    - https://www.it-swarm.dev/ja/python/sqlalchemy%E3%81%A7sql%E3%83%93%E3%83%A5%E3%83%BC%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95%E3%81%AF%EF%BC%9F/941845648/
    - https://stackoverflow.com/questions/9766940/how-to-create-an-sql-view-with-sqlalchemy

