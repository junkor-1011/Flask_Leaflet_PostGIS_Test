#!/bin/bash

docker-compose run app_flask /bin/bash -c "python init_db.py"

