#!/usr/bin/env bash
# https://qiita.com/A-Kira/items/3339e902e7a8fca8fdf6


# 実行スクリプトのpath取得
# https://qiita.com/koara-local/items/2d67c0964188bba39e29
SCRIPT_DIR=$(cd $(dirname $0); pwd)
cd $SCRIPT_DIR


# DEFAULT ARGS
POSTGRES_USER=test_user
POSTGRES_DB=test_db
PORT=15432
HOSTNAME=localhost

# https://qiita.com/b4b4r07/items/dcd6be0bb9c9185475bb
# https://qiita.com/ko1nksm/items/cea7e7cfdc9e25432bab
args=`getopt -o U:d:h:p -l user:db:host:port -- "$@"`

if [ $? != 0 ]; then
    echo "Usage: $0 [-p port | --port port | -U user | --user user] " 1>&2
    exit 1
fi
#set -- $args
eval "set -- $args"
for OPT in "$@"
do
    case $OPT in
#        -a) A_FLAG=1
#            shift
#            ;;
        -U | --user) POSTGRES_USER=$2
            shift 2
            ;;
        -d | --db) POSTGRES_DB=$2
            shift 2
            ;;
        -p | --port) PORT=$2
            shift 2
            ;;
        -h | --host) HOSTNAME=$2
            shift 2
            ;;
        --) shift
            break
            ;;
    esac
done

#psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} < "/docker-entrypoint-initdb.d/create-tables.sql"
#psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} < "/docker-entrypoint-initdb.d/insert-data.sql"


# iris
psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -h ${HOSTNAME} -p ${PORT} -f "./insert-iris.sql"

# dots
psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -h ${HOSTNAME} -p ${PORT} -f "./insert-dots.sql"

# flights
psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -h ${HOSTNAME} -p ${PORT} -f "./insert-flights.sql"


