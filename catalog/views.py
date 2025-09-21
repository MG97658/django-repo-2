from django.shortcuts import render
from catalog.models import Book, Author, BookInstance
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic 


# Create your views here.
def index(request):
    """View function for home page of site."""
    
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default
    num_authors = Author.objects.count()
    
    # Number of visits to this view, as counted in the session variable
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)
# Generic class-based views for Book
class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = 'catalog/book_list.html'  # optional: specify your template
    context_object_name = 'book_list'         # optional: default is 'object_list'
    paginate_by = 10                           # optional: pagination

class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'  # optional
# Generic class-based views for Author
class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    template_name = 'catalog/author_list.html'  # optional
    context_object_name = 'author_list'         # optional
    paginate_by = 10                            # optional: pagination

class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author
    template_name = 'catalog/author_detail.html'  # optional



