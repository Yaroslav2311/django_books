from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
app = Celery('mysite')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'add-every-2-hours': {
#         'task': 'tasks.create_note',
#         'schedule': 30.0,# crontab(minute=0, hour='1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23')
#     },
# }
