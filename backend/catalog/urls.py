# catalog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("books/", views.book_list, name="book_list"),
    path("books/<int:book_id>/", views.book_detail, name="book_detail"),

    # thêm các đường dẫn CRUD cho Book
    path("books/add/", views.book_create, name="book_create"),
    path("books/<int:pk>/edit/", views.book_update, name="book_update"),
    path("books/<int:pk>/delete/", views.book_delete, name="book_delete"),
    
    # Borrowers
    path("borrowers/", views.borrower_list, name="borrower_list"),
    path("borrowers/add/", views.borrower_create, name="borrower_create"),
    path("borrowers/<int:pk>/edit/", views.borrower_update, name="borrower_update"),
    path("borrowers/<int:pk>/delete/", views.borrower_delete, name="borrower_delete"),
    path("borrow/confirm/<int:pk>/", views.confirm_return, name="confirm_return"),


    # Loans
    path("loans/", views.loan_list, name="loan_list"),
    path("loans/add/", views.loan_create, name="loan_create"),
    path("loans/<int:pk>/edit/", views.loan_update, name="loan_update"),
    path("loans/<int:pk>/delete/", views.loan_delete, name="loan_delete"),

    # Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),

    # catalog/urls.py

# Author
path("authors/", views.author_list, name="author_list"),
path("authors/add/", views.author_create, name="author_create"),
path("authors/<int:pk>/edit/", views.author_update, name="author_update"),
path("authors/<int:pk>/delete/", views.author_delete, name="author_delete"),

# Category
path("categories/", views.category_list, name="category_list"),
path("categories/add/", views.category_create, name="category_create"),
path("categories/<int:pk>/edit/", views.category_update, name="category_update"),
path("categories/<int:pk>/delete/", views.category_delete, name="category_delete"),

# Publisher
path("publishers/", views.publisher_list, name="publisher_list"),
path("publishers/add/", views.publisher_create, name="publisher_create"),
path("publishers/<int:pk>/edit/", views.publisher_update, name="publisher_update"),
path("publishers/<int:pk>/delete/", views.publisher_delete, name="publisher_delete"),

path("metadata/", views.manage_metadata, name="manage_metadata"),

]
