# CRUD Operations for Book Model

This document summarizes the CRUD operations performed on the `Book` model within the Django app `bookshelf`.

## Create
To create a `Book` instance, the following command was used:
```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()

Expected output: <Book: 1984>