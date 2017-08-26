FROM python:3.6

WORKDIR /usr/src/app
RUN pip install django Pillow
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
