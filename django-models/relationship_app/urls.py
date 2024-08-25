from django.urls import path
from .views import list_books, LibraryDetailView  # Import the views
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import views from the current app

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Route for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Route for the class-based view
    path('register/', views.register, name='register'),  # Route for user registration
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Route for user login
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Route for user logout
]
