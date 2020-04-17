-- https://qiita.com/A-Kira/items/3339e902e7a8fca8fdf6
INSERT INTO test_table (gid, geom) SELECT 1, ST_GeomFromText('POINT(135 35)', 4612);
