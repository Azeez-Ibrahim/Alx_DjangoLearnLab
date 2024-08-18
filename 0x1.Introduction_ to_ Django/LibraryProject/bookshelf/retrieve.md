
### `retrieve.md`
```markdown
# Retrieve Operation

This document details the process of retrieving the `Book` instance created in the Django app `bookshelf`.

## Command Used
```python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

Expected output: 1984 George Orwell 1949
