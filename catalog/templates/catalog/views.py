# catalog/views.py
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    """View function for home page of site."""
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    # session visit count:
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    return render(request, 'catalog/index.html', context=context)

# Class-based views for list/detail
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10   # optional pagination

class BookDetailView(generic.DetailView):
    model = Book

# Optional Author views (to implement "All Authors")
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author
