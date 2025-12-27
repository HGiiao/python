from django.shortcuts import render
from django.db.models import Count
from .models import Book, Borrower, Loan, Author

def home(request):
    return render(request, "catalog/home.html", {})

def book_list(request):
    query = request.GET.get("q")
    books = Book.objects.select_related("author", "category", "publisher")
    if query:
        books = books.filter(title__icontains=query)
    else:
        books = books.all()
    return render(request, "catalog/book_list.html", {"books": books})

from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookForm
from .models import Book

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "catalog/book_form.html", {"form": form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "catalog/book_form.html", {"form": form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "catalog/book_confirm_delete.html", {"book": book})

def book_detail(request, book_id):
    book = Book.objects.select_related("author", "category", "publisher").get(id=book_id)
    return render(request, "catalog/book_detail.html", {"book": book})

from django.shortcuts import redirect
from .forms import BorrowerForm, LoanForm
from .models import Loan

def borrower_create(request):
    if request.method == "POST":
        form = BorrowerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("borrower_list")
    else:
        form = BorrowerForm()
    return render(request, "catalog/borrower_form.html", {"form": form})

def borrower_list(request):
    borrowers = Borrower.objects.all()
    return render(request, "catalog/borrower_list.html", {"borrowers": borrowers})

def loan_create(request):
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loan_list")
    else:
        form = LoanForm()
    return render(request, "catalog/loan_form.html", {"form": form})

def loan_list(request):
    loans = Loan.objects.select_related("book", "borrower").all()
    return render(request, "catalog/loan_list.html", {"loans": loans})

def dashboard(request):
    stats = {
        "books": Book.objects.count(),
        "authors": Author.objects.count(),
        "borrowers": Borrower.objects.count(),
        "loans": Loan.objects.count(),
    }

    # Đếm số lượt mượn theo tháng
    monthly_loans = Loan.objects.values("borrow_date__month").annotate(total=Count("id")).order_by("borrow_date__month")
    loan_counts = [0] * 12
    for item in monthly_loans:
        month = item["borrow_date__month"]
        loan_counts[month - 1] = item["total"]

    context = {
        "stats": stats,
        "loan_counts": loan_counts,
    }
    return render(request, "catalog/dashboard.html", context)

# --- BORROWER UPDATE & DELETE ---
def borrower_update(request, pk):
    borrower = get_object_or_404(Borrower, pk=pk)
    if request.method == "POST":
        form = BorrowerForm(request.POST, instance=borrower)
        if form.is_valid():
            form.save()
            return redirect("borrower_list")
    else:
        form = BorrowerForm(instance=borrower)
    return render(request, "catalog/borrower_form.html", {"form": form})

def borrower_delete(request, pk):
    borrower = get_object_or_404(Borrower, pk=pk)
    if request.method == "POST":
        borrower.delete()
        return redirect("borrower_list")
    return render(request, "catalog/borrower_confirm_delete.html", {"borrower": borrower})


# --- LOAN UPDATE & DELETE ---
def loan_update(request, pk):
    loan = get_object_or_404(Loan, pk=pk)
    if request.method == "POST":
        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            form.save()
            return redirect("loan_list")
    else:
        form = LoanForm(instance=loan)
    return render(request, "catalog/loan_form.html", {"form": form})

def loan_delete(request, pk):
    loan = get_object_or_404(Loan, pk=pk)
    if request.method == "POST":
        loan.delete()
        return redirect("loan_list")
    return render(request, "catalog/loan_confirm_delete.html", {"loan": loan})

# catalog/views.py
from .models import Author, Category, Publisher
from .forms import AuthorForm, CategoryForm, PublisherForm

# --- AUTHOR ---
def author_list(request):
    authors = Author.objects.all()
    return render(request, "catalog/author_list.html", {"authors": authors})

def author_create(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("author_list")
    return render(request, "catalog/author_form.html", {"form": form})

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    form = AuthorForm(request.POST or None, instance=author)
    if form.is_valid():
        form.save()
        return redirect("author_list")
    return render(request, "catalog/author_form.html", {"form": form})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        author.delete()
        return redirect("author_list")
    return render(request, "catalog/author_confirm_delete.html", {"author": author})

# --- CATEGORY ---
def category_list(request):
    categories = Category.objects.all()
    return render(request, "catalog/category_list.html", {"categories": categories})

def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("category_list")
    return render(request, "catalog/category_form.html", {"form": form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect("category_list")
    return render(request, "catalog/category_form.html", {"form": form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect("category_list")
    return render(request, "catalog/category_confirm_delete.html", {"category": category})

# --- PUBLISHER ---
def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, "catalog/publisher_list.html", {"publishers": publishers})

def publisher_create(request):
    form = PublisherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("publisher_list")
    return render(request, "catalog/publisher_form.html", {"form": form})

def publisher_update(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    form = PublisherForm(request.POST or None, instance=publisher)
    if form.is_valid():
        form.save()
        return redirect("publisher_list")
    return render(request, "catalog/publisher_form.html", {"form": form})

def publisher_delete(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == "POST":
        publisher.delete()
        return redirect("publisher_list")
    return render(request, "catalog/publisher_confirm_delete.html", {"publisher": publisher})
from .models import Author, Category, Publisher

from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

def confirm_return(request, pk):
    record = get_object_or_404(BorrowRecord, pk=pk)
    if request.method == "POST":
        record.return_date = timezone.now().date()
        record.save()
    return redirect("borrow_list")

    from django.utils import timezone

def confirm_return(request, pk):
    loan = get_object_or_404(Loan, pk=pk)
    if request.method == "POST":
        loan.return_date = timezone.now().date()
        loan.save()
    return redirect("loan_list")



def manage_metadata(request):
    authors = Author.objects.all()
    categories = Category.objects.all()
    publishers = Publisher.objects.all()
    return render(
        request,
        "catalog/manage_metadata.html",
        {
            "authors": authors,
            "categories": categories,
            "publishers": publishers,
        },
    )
