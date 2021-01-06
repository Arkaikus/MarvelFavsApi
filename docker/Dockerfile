FROM python:3.8

RUN apt update \
&& apt install nano \
&& pip3 install -U pip setuptools \
&& pip install --upgrade pip

COPY app /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip3 install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate
