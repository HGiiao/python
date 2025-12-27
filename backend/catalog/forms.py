# catalog/forms.py
from django import forms
from .models import Book, Borrower, Loan

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        author = cleaned_data.get("author")

        # Kiểm tra trùng tên sách + tác giả
        if Book.objects.filter(title=title, author=author).exists():
            raise forms.ValidationError("❌ Sách này đã tồn tại trong hệ thống!")

        return cleaned_data


class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = "__all__"

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Borrower.objects.filter(email=email).exists():
            raise forms.ValidationError("❌ Email này đã được đăng ký!")
        return email


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        borrower = cleaned_data.get("borrower")
        book = cleaned_data.get("book")

        if Loan.objects.filter(borrower=borrower, book=book, returned=False).exists():
            raise forms.ValidationError("❌ Độc giả này đã mượn sách này và chưa trả!")
        return cleaned_data


# catalog/forms.py
from django import forms
from .models import Author, Category, Publisher

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if Author.objects.filter(name=name).exists():
            raise forms.ValidationError("❌ Tác giả này đã tồn tại!")
        return name


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if Category.objects.filter(name=name).exists():
            raise forms.ValidationError("❌ Thể loại này đã tồn tại!")
        return name


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if Publisher.objects.filter(name=name).exists():
            raise forms.ValidationError("❌ Nhà xuất bản này đã tồn tại!")
        return name


