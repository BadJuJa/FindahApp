from django.shortcuts import render

def index(request):
    return render(request, 'simFindah/index.html')

from .vector_search import search_vector
from .book_search import search

def search_result(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        isbns = search_vector(searched)
        books = search(isbns)
        context = {'searched': searched,
        'books': books}
        return render(request, 'simFindah/search_result.html', context)
    else:
        context = {}
        return render(request, 'simFindah/search_result.html', context)

def search_view(request, *args, **kwargs):
    return render(request, 'simFindah/index.html', {})