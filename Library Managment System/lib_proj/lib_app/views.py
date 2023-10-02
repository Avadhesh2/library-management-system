from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Book
# Create your views here.


def home(request):
    bks = Book.objects.all()
    context = {
        'bks': bks
    }
    # print(context)
    return render(request, 'home.html', context)


def addBook(request):
    if request.method == 'POST':
        title = request.POST['title']
        price = int(request.POST['price'])

        new_book = Book(title=title, price=price)

        new_book.save()
        return HttpResponseRedirect('/')

    elif request.method == 'GET':  # show all the entry which  is we are going to fill in form
        return render(request, 'addBook.html')

    else:
        return HttpResponse("An Exception Occured! Book Has Not Been Added")


def editBook(request):
    if request.method == 'POST':
        title = request.POST['title']
        price = int(request.POST['price'])
        # Changed to lowercase 'post' in 'request.POST'
        book_id = int(request.POST['bookid'])

        try:
            edit_book = Book.objects.get(id=book_id)
            edit_book.title = title  # Update the existing book's attributes
            edit_book.price = price

            edit_book.save()
            return HttpResponseRedirect('/')
        except Book.DoesNotExist:
            return HttpResponse("Book not found")

    elif request.method == 'GET':
        return render(request, 'edit_book.html')


def editBookView(request):
    book = Book.objects.get(id=request.GET['bookid'])
    return render(request, "edit_book.html", {"book": book})


def deleteBookView(request):
    book = Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/')
