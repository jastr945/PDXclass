python3 manage.py migrate
uwsgi --chdir=./ --module=animalproject.wsgi:application --env DJANGO_SETTINGS_MODULE=animalproject.settings --socket=/tmp/animalproject.sock --master --http :80s
