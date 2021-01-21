from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import NewBookForm, BorrowBookForm
from .models import Book, Author

# Create your views here.
def homepage(req):
    data = { 'books': Book.objects.all() }
    return render(req, 'books/home.html', data)


def not_found_404(request, exception):
    data = { 'err': exception}
    return render(request, 'adoption/404.html', data)

@login_required
def create(request):
    if request.method == 'POST':
        book = NewBookForm(request.POST)
        if book.is_valid():
            book_id = book.save().id
            return redirect("books-show", book_id=book_id)
    else:
        form = NewBookForm()
    data = {'form': form}
    return render(request, 'books/new.html', data)


@login_required
def show(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            book.borrower = request.user
            book.save()
            return redirect('books-show', book_id=book_id)
    else:
        form = BorrowBookForm(initial={'borrower': request.user})
    data = {
        'book': book,
        'form': form
    }
    return render(request, 'books/book_by_id.html', data)
   