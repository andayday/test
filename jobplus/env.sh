#!/bin/bash
export FLASK_APP=manage.py
export FLASK_DEBUG=True

flask run -h "0.0.0.0"

