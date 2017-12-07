python3 manage.py migrate
python3 manage.py loaddata fixturefile.json
uwsgi --chdir=./ --module=myportfolio.wsgi:application --env DJANGO_SETTINGS_MODULE=myportfolio.settings --socket=/tmp/myportfolio.sock --master --http :80
