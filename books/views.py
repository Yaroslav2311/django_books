from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count, Max
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Author, Book, Publisher, Store


def all_books(request):
    all_book = Book.objects.select_related('publisher').all()
    max_price = Book.objects.aggregate(Max('price'))['price__max']
    avg_rat = Book.objects.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'books/all_books.html', {'all_book': all_book, 'max_price': max_price, 'avg_rat': avg_rat})


# def all_author(request):
#     all_authors = Author.objects.prefetch_related('book_set__authors').all()
#     return render(request, 'books/all_author.html', {'all_authors': all_authors})
class AllAuthor(ListView):
    model = Author
    template_name = 'books/all_author.html'
    # all_authors = Author.objects.prefetch_related('book_set__authors').all()
    context_object_name = 'all_authors'
    extra_context = {'title': 'List of all authors'}
    paginate_by = 5


class AddAuthor(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name', 'age']
    template_name = 'books/create_author.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('books:all_author')


class UpdateAuthor(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['name', 'age']
    template_name = 'books/update_author.html'
    # pk_url_kwarg = 'pk'
    # success_url = reverse_lazy('books:author', kwargs={'pk': pk_url_kwarg})
    success_url = reverse_lazy('books:all_author')


class DelAuthor(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'books/delete_author.html'
    # success_url = '/books/author'
    success_url = reverse_lazy('books:all_author')


class OneAuthor(DetailView):
    model = Author
    template_name = 'books/one_author.html'
    context_object_name = 'context'


def all_publisher(request):
    obj = Publisher.objects.prefetch_related('book_set').annotate(num_book=Count('book')).all()
    return render(request, 'books/all_publisher.html', {'obj': obj})


def all_store(request):
    obj = Store.objects.prefetch_related('books').all()
    return render(request, 'books/all_store.html', {'obj': obj})


def book(request, pk):
    obj = get_object_or_404(Book.objects.select_related('publisher'), pk=pk)
    return render(request, 'books/look_book.html', {'obj': obj})


def one_publisher(request, pk):
    obj = get_object_or_404(Publisher, pk=pk)
    return render(request, 'books/one_publisher.html', {'obj': obj})


def store(request, pk):
    obj = get_object_or_404(Store, pk=pk)
    return render(request, 'books/store.html', {'obj': obj})
