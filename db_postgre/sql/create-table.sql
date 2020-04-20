-- ref: https://qiita.com/A-Kira/items/3339e902e7a8fca8fdf6
-- 拡張をインストール
CREATE EXTENSION IF NOT EXISTS postgis;

-- テーブル削除
DROP TABLE IF EXISTS test_table;

-- テーブル作成
CREATE TABLE IF NOT EXISTS test_table
(
    gid    INTEGER PRIMARY KEY,
    geom   GEOMETRY(POINT, 4612)
);


