python3 manage.py migrate
uwsgi --chdir=./ --module=myportfolio.wsgi:application --env DJANGO_SETTINGS_MODULE=myportfolio.settings --socket=/tmp/myportfolio.sock --master --http :80
