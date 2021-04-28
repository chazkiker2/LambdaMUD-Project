release: python manage.py shell < ./util/heroku_release.py
web: gunicorn adv_project.wsgi:application --log-file -