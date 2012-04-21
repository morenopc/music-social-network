#!/bin/sh

WORKON_HOME=/home/moreno/.virtualenvs
PROJECT_ROOT=/home/moreno/apps_wsgi/dev

# activate virtual environment
. $WORKON_HOME/pinax-dev/bin/activate

cd $PROJECT_ROOT
python manage.py send_mail >> $PROJECT_ROOT/logs/cron_mail.log 2>&1
