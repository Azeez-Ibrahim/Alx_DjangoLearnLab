
### `update.md`
```markdown
# Update Operation

This document details the process of updating the title of the `Book` instance in the Django app `bookshelf`.

## Command Used
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

Expected output: <Book: Nineteen Eighty-Four>
