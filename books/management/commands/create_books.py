import random

from books.models import Author, Book, Publisher, Store

from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):

    def handle(self, *args, **options):
        Publisher.objects.all().delete()
        Book.objects.all().delete()
        Store.objects.all().delete()
        Author.objects.all().delete()

        publishers = [Publisher(name=f"Publisher{index}") for index in range(1, 6)]
        Publisher.objects.bulk_create(publishers)

        authors = []
        for i in range(1, 11):
            authors.append(Author(name=f'Author{i}', age=random.randint(30, 75)))
        Author.objects.bulk_create(authors)

        fake = Faker()
        counter = 0
        books = []
        for publisher in Publisher.objects.all():
            for i in range(20):
                counter = counter + 1
                book_one = Book(name=f"Book{counter}", price=random.randint(50, 700), pages=random.randint(190, 1200), rating=round(random.uniform(3, 5), 3), publisher=publisher, pubdate=fake.date_time_between(start_date='-30y', end_date='now'))
                book_one.save()
                book_one.authors.set(random.choices(list(Author.objects.all()), k=random.randint(1, 3)))
                book_one.save()

        books = list(Book.objects.all())
        for i in range(10):
            temp_books = [books.pop(0) for i in range(10)]
            store = Store.objects.create(name=f"Store{i+1}")
            store.books.set(temp_books)
            store.save()
