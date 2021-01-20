from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# from .models import Book

books = [
        { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
        { 'id': 2, 'title': 'The Meaning of Liff', 'author': 'Douglas Adams'},
        { 'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'}
    ]

# Create your views here.

def index(req):
    return HttpResponse("<h1>Hello! Here are all the books!<h1>")

def show(req, id):
    return HttpResponse(f'<h3>Book number {books.id}: {books.title} by {books.author}</h3>')

def not_found_404(request, exception):
    data = { 'err': exception}
    return render(request, 'adoption/404/html', data)

def home(request):
    # data = { 'books': Book.objects.all() }
    
    return render(request, 'books/home.html', data)