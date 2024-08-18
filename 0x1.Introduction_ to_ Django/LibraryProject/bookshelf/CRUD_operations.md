```
Python 3.12.4 (main, Jun  6 2024, 18:26:44) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book.save()
>>> book = Book.objects.get(title="1984")
>>> print(book.title, book.author, book.publication_year)
1984 George Orwell 1949
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> books = Book.objects.all()
>>> print(books)
<QuerySet []>
>>> 
```