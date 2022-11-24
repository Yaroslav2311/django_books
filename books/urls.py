from django.urls import path

from .views import AddAuthor, AllAuthor, DelAuthor, OneAuthor, UpdateAuthor, all_books, all_publisher, all_store, book, one_publisher, store


app_name = 'books'
urlpatterns = [
    path('book', all_books, name='all_books'),
    path('author', AllAuthor.as_view(), name='all_author'),
    path('author/create', AddAuthor.as_view(), name='add_author'),
    path('author/<int:pk>/update', UpdateAuthor.as_view(), name='up_author'),
    path('author/<int:pk>/delete', DelAuthor.as_view(), name='delauthor'),
    path('publisher', all_publisher, name='all_publisher'),
    path('store', all_store, name='all_store'),
    path('book/<int:pk>', book, name='book'),
    path('publisher/<int:pk>', one_publisher, name='one_publisher'),
    path('author/<int:pk>', OneAuthor.as_view(), name='author'),
    path('store/<int:pk>', store, name='store'),

]
