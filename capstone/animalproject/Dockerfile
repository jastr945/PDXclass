FROM python:3.6

WORKDIR /usr/src/app
RUN pip install django Pillow uwsgi django-taggit django-multiselectfield django-filter django-cleanup WhiteNoise django_unused_media
COPY . .
RUN python3 manage.py collectstatic --noinput

EXPOSE 80
CMD . /usr/src/app/startserver.sh
