#!/bin/sh

redis-server >> /dev/null &
python manage.py runserver >> /dev/null &
python manage.py rqworker shipyard >> /dev/null &
