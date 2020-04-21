#!/usr/bin/env bash
# https://qiita.com/A-Kira/items/3339e902e7a8fca8fdf6


# 実行スクリプトのpath取得
# https://qiita.com/koara-local/items/2d67c0964188bba39e29
SCRIPT_DIR=$(cd $(dirname $0); pwd)
cd $SCRIPT_DIR


# DEFAULT ARGS
MYSQL_USER=test_user
MYSQL_DB=test_db
PORT=13306
HOST=127.0.0.1
PASSWD=password

# https://qiita.com/b4b4r07/items/dcd6be0bb9c9185475bb
# https://qiita.com/ko1nksm/items/cea7e7cfdc9e25432bab
args=`getopt -o u:d:h:p -l user:db:host:port -- "$@"`

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
        -u | --user) MYSQL_USER=$2
            shift 2
            ;;
        -d | --db) MYSQL_DB=$2
            shift 2
            ;;
        -P | --port) PORT=$2
            shift 2
            ;;
        -h | --host) HOST=$2
            shift 2
            ;;
        --) shift
            break
            ;;
    esac
done


# iris
mysql -u ${MYSQL_USER} -h ${HOST} -P ${PORT} -p -D ${MYSQL_DB} < "./insert-iris.sql"
                                                      
# dots                                                
mysql -u ${MYSQL_USER} -h ${HOST} -P ${PORT} -p -D ${MYSQL_DB} < "./insert-dots.sql"
                                                      
# flights                                             
mysql -u ${MYSQL_USER} -h ${HOST} -P ${PORT} -p -D ${MYSQL_DB} < "./insert-flights.sql"


# geo_point_test_a                                             
mysql -u ${MYSQL_USER} -h ${HOST} -P ${PORT} -p -D ${MYSQL_DB} < "./insert-geo_point_test_a.sql"

