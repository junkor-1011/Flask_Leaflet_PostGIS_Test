-- MySQL
-- dots from seaborn
-- https://www.virment.com/sql-for-import-csv-mysql/
load data local infile "./dots.csv" into table dots fields terminated by ',' optionally enclosed by '"' ignore 1 lines
(@id,@align,@choice,@time,@coherence,@firing_rate)

set id = @id,
align = @align,
choice = @choice,
time = @time,
coherence = @coherence,
firing_rate = @firing_rate;
