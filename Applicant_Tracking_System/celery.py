import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Applicant_Tracking_System.settings")

app = Celery("Applicant_Tracking_System")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
