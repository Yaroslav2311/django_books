from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help = 'creating random users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, choices=range(11))

    def handle(self, *args, **options):
        User = get_user_model()
        fake = Faker()
        cr_users = []
        count = options['count']
        for i in range(count):
            cr_users.append(User(email=fake.email(), username=fake.name(), password=fake.password()))
        User.objects.bulk_create(cr_users)
