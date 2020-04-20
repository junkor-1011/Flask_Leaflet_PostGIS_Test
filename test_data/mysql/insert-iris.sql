-- PostgreSQL
-- iris from seaborn
-- https://www.virment.com/sql-for-import-csv-mysql/
load data local infile "./iris.csv" into table iris fields terminated by ',' optionally enclosed by '"' ignore 1 lines
(@id,@sepal_length,@sepal_width,@petal_length,@petal_width,@species)

set id = @id,
sepal_length = @sepal_length,
sepal_width = @sepal_width,
petal_length = @petal_length,
petal_width = @petal_width,
species = @species;
