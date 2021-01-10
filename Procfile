release: python app/manage.py makemigrations --noinput && python app/manage.py migrate --noinput
web: gunicorn app.wsgi --chdir app/ --log-file -