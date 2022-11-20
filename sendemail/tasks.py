from __future__ import absolute_import, unicode_literals

from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail

import requests

from .models import Authors, Phrases


@shared_task
def send_email(subject, text, from_email, email):
    send_mail(subject, text, from_email, email)


@shared_task
def create_note():

    phrase_list = []
    author_list = []
    page = 1
    while len(phrase_list) < 5:
        url = f'https://quotes.toscrape.com/page/{page}/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for x in soup.find_all('div', class_='quote'):
            if len(phrase_list) < 5:
                # if x.find('span', class_='text').text not in phrases_in_db:
                try:
                    Phrases.objects.get(phrase=x.find('span', class_='text').text)
                except Exception:
                    phrase_list.append(x.find('span', class_='text').text)
                    author_list.append(x.find('small', class_='author').text)
        if soup.find('li', class_='next'):
            page += 1
        else:
            break
    phrases = []
    if len(phrase_list) < 5:
        raise Exception('no more objects')
    for i in range(len(phrase_list)):
        ab = Authors.objects.get_or_create(name=author_list[i])
        phrases.append(Phrases(phrase=phrase_list[i], author=ab[0]))
    Phrases.objects.bulk_create(phrases)
