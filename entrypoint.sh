#!/usr/bin/env bash
set -e
python manage.py collectstatic --noinput || true
python manage.py migrate --noinput
gunicorn Applicant_Tracking_System.wsgi:application -b 0.0.0.0:8000 --workers 3
