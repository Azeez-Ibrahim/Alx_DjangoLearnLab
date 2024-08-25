from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)  # Filtering books by the author
    return books

# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Using the related_name 'libraries'
    return books

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # Using the related_name 'librarian'
    return librarian

# Sample outputs
if __name__ == "__main__":
    # Replace with actual values in your database
    print("Books by George Orwell:")
    for book in get_books_by_author("George Orwell"):
        print(book.title)

    print("\nBooks in Central Library:")
    for book in list_books_in_library("Central Library"):
        print(book.title)

    print("\nLibrarian of Central Library:")
    librarian = get_librarian_for_library("Central Library")
    print(librarian.name)
