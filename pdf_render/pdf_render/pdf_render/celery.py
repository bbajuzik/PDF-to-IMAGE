from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery("pdf_render")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
