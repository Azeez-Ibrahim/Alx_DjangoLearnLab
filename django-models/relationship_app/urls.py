from django.urls import path
from .views import list_books, LibraryDetailView  # Import the views
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import views from the current app
from .views.admin_view import admin_view
from .views.librarian_view import librarian_view
from .views.member_view import member_view

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Route for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Route for the class-based view
    path('register/', views.register, name='register'),  # Route for user registration
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Route for user login
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Route for user logout
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]
