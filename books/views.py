import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from books.models import Book, Publisher, Author
from django.views.generic import ListView, DetailView


class AuthorDetailView(DetailView):
    queryset = Author.objects.all()

    def get_object(self):
        #call the superclass
        object = super(AuthorDetailView,self).get_object()
        #record last accessed date
        object.last_accessed = datetime.datetime.now()
        object.save()
        return object
        
class PublisherBookListView(ListView):
    context_object_name = 'book_list'
    template_name= "books/books_by_publisher.html"
    
    def get_queryset(self):
       self.publisher = get_object_or_404(Publisher, name__iexact=self.args[0])
       return Book.objects.filter(publisher=self.publisher)
    
    def get_context_data(self, **kwargs):
        context = super(PublisherBookListView,self).get_context_data(**kwargs)
        context['publisher'] = self.publisher
        return context
        
def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request,'search_results.html',
            {'books': books, 'query':q })
    else:
        return render(request, 'search_form.html',{'error':True})
        
