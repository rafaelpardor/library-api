#!/bin/bash
echo "Wating to connect to postgres..."
while ! nc -z books_db 5432; do
  echo "Reaching to database..."
  sleep 0.5
done
echo "Connected to database."

python manage.py run -h 0.0.0.0 -p 5002
