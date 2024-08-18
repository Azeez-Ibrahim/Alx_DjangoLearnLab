
### `delete.md`
```markdown
# Delete Operation

This document details the process of deleting the `Book` instance in the Django app `bookshelf`.

## Command Used
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Expected output: (1, {'bookshelf.Book': 1})
