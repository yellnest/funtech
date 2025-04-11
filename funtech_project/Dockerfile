FROM python:3.11-slim

# install system dependencies
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD python manage.py makemigrations --settings=backend.settings.prod \
    && python manage.py migrate --settings=backend.settings.prod \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'root@example.com', '123')" --settings=backend.settings.prod \
    && python manage.py collectstatic --noinput --settings=backend.settings.prod \
    && gunicorn backend.wsgi:application --bind 0.0.0.0:8000

