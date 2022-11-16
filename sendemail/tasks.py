from __future__ import absolute_import, unicode_literals

from celery import shared_task

from django.core.mail import send_mail


@shared_task
def send_email(subject, text, from_email, email):
    send_mail(subject, text, from_email, email)
