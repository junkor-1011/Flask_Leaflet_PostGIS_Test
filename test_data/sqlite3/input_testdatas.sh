#!/usr/bin/env bash
# https://qiita.com/A-Kira/items/3339e902e7a8fca8fdf6


# 実行スクリプトのpath取得
# https://qiita.com/koara-local/items/2d67c0964188bba39e29
SCRIPT_DIR=$(cd $(dirname $0); pwd)
cd $SCRIPT_DIR


# DEFAULT ARGS
PATH_DB=$SCRIPT_DIR/../../db_sqlite3/data.sqlite3

# https://qiita.com/b4b4r07/items/dcd6be0bb9c9185475bb
# https://qiita.com/ko1nksm/items/cea7e7cfdc9e25432bab
args=`getopt -o p: -l path-db: -- "$@"`

if [ $? != 0 ]; then
    echo "Usage: $0 [-p path_db | --path-db path_db] " 1>&2
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
        -p | --path-db) PATH_DB=$2
            shift 2
            ;;
        --) shift
            break
            ;;
    esac
done


# iris
sqlite3 $PATH_DB < "./insert-iris.sql"
                                                      
# dots                                                
sqlite3 $PATH_DB < "./insert-dots.sql"
                                                      
# flights                                             
sqlite3 $PATH_DB < "./insert-flights.sql"


