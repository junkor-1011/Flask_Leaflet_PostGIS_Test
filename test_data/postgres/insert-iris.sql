-- PostgreSQL
-- iris from seaborn
-- https://kanamelogic.com/20180211/postgresql-copy2/
\copy iris(id, sepal_length, sepal_width, petal_length, petal_width, species) from './iris.csv' with csv header
