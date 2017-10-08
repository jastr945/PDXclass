FROM python:3.6

WORKDIR /usr/src/app
RUN pip install django Pillow uwsgi taggit multiselectfield django_filters django_cleanup django_unused_media
COPY . .
RUN python3 manage.py collectstatic

EXPOSE 80
CMD . /usr/src/app/startserver.sh
