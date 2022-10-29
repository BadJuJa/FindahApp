from .models import Books
def search(results):
    isbns = results
    books = []
    for isbncode in isbns['matches']:
        books.append(Books.objects.filter(isbn__contains=isbncode['id'], link__contains="book24"))
    return books