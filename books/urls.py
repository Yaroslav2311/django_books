from django.urls import path

from .views import all_author, all_books, all_publisher, all_store, book, one_author, one_publisher, store


app_name = 'books'
urlpatterns = [
    path('book', all_books, name='all_books'),
    path('author', all_author, name='all_author'),
    path('publisher', all_publisher, name='all_publisher'),
    path('store', all_store, name='all_store'),
    path('book/<int:pk>', book, name='book'),
    path('publisher/<int:pk>', one_publisher, name='one_publisher'),
    path('author/<int:pk>', one_author, name='author'),
    path('store/<int:pk>', store, name='store'),

]
