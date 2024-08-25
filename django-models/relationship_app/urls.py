from django.urls import path
from .views import list_books, LibraryDetailView  # Import the views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Route for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Route for the class-based view
]
