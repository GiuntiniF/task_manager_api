web: python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn task_manager_api.wsgi --log-file -