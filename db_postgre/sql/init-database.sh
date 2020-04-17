#!/usr/bin/env bash
# https://qiita.com/A-Kira/items/3339e902e7a8fca8fdf6

#psql -U postgres -d postgres < "/docker-entrypoint-initdb.d/create-tables.sql"
#psql -U postgres -d postgres < "/docker-entrypoint-initdb.d/insert-data.sql"

psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} < "/docker-entrypoint-initdb.d/create-tables.sql"
psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} < "/docker-entrypoint-initdb.d/insert-data.sql"
