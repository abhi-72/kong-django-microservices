#!/bin/bash

# Check if rabbit is up and running before starting the service.

until nc -z ${RABBIT_HOST} ${RABBIT_PORT}; do
    echo "$(date) - waiting for rabbitmq..."
    sleep 2
done

# Run Nameko service
nameko run --config rabbitmq_config.yml service --backdoor 3000 &

# Run Django service
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

