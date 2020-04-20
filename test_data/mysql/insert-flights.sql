-- PostgreSQL
-- flights from seaborn
-- https://www.virment.com/sql-for-import-csv-mysql/
load data local infile "./flights.csv" into table flights fields terminated by ',' optionally enclosed by '"' ignore 1 lines
(@year,@month,@passengers)

set year = @year,
month = @month,
passengers = @passengers;

