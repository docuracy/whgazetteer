#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

# Create debug log file
mkdir -p /app/whg/logs
touch /app/whg/logs/debug.log
chmod 777 /app/whg/logs/debug.log

# Build database tables from Django models
python manage.py makemigrations
python manage.py migrate

# Create a superuser account
python manage.py createsuperuser

# Start the development server
python manage.py runserver 0.0.0.0:8000

# Populate database tables for basic operation
psql -h ${DB_HOST} -p ${DB_PORT} -d ${DB_NAME} < docs/cloning/types.sql
psql -h ${DB_HOST} -p ${DB_PORT} -d ${DB_NAME} < docs/cloning/combined.sql

# Gather static files into the 'static/' directory
python manage.py collectstatic --no-input