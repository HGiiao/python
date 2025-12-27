from django.contrib import admin
from .models import Author, Category, Publisher, Book, Borrower, Loan

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Borrower)
admin.site.register(Loan)
