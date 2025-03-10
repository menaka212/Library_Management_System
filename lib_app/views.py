from django.shortcuts import render, get_object_or_404, redirect
from .models import Book1
from .forms import BookForm

def home_view(request):
    """ Renders the home page """
    return render(request, 'home.html')

def add_book(request):
    """ Adds a new book to the database """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def book_list(request):
    """ Displays the list of books """
    books = Book1.objects.all()
    return render(request, 'book_list.html', {'books': books})

def edit_book(request, book_id):
    """ Edits an existing book """
    book = get_object_or_404(Book1, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})
