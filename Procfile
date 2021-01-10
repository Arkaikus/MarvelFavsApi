release: python app/manage.py makemigrations && python app/manage.py makemigrations api && python app/manage.py migrate --noinput
web: gunicorn app.wsgi --chdir app/ --log-file -