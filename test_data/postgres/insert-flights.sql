-- PostgreSQL
-- flights from seaborn
-- https://kanamelogic.com/20180211/postgresql-copy2/
\copy flights(year, month, passengers) from './flights.csv' with csv header
