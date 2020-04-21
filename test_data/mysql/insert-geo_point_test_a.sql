-- MySQL
-- https://www.virment.com/sql-for-import-csv-mysql/
load data local infile "./geo_point_test_a.csv" into table geo_point_test_a fields terminated by ',' optionally enclosed by '"' ignore 1 lines
(@id,@name,@order,@p_type,@latitude,@longitude,@val_int,@val_float,@timestamp,@ts_int,@created_at,@updated_at,@date)

set id = @id,
name = @name,
`order` = @order,
p_type = @p_type,
latitude = @latitude,
longitude = @longitude,
val_int = @val_int,
val_float = @val_float,
timestamp = @timestamp,
ts_int = @ts_int,
created_at = @created_at,
updated_at = @updated_at,
date = @date;
