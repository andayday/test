#!/bin/bash
# readme usage: source env.sh
export FLASK_APP=manage.py
export FLASK_DEBUG=True

flask run -h "0.0.0.0"

#update db
#flask db migrate 
#flask db upgrade

#mysql 
#show create table table_name;

