from django.shortcuts import render, redirect
from django.http import HttpResponse
from books.models import Book
from books.forms import BookForm

# helper function
def get_book(book_id):
    return Book.objects.get(id=book_id)

# route functions
def book_list(request):
    books = Book.objects.all()
    data = {'all_books': books }
    return render(request, 'books/book_list.html', data)

def book_view(request, book_id):
    book = get_book(book_id)
    data = {'book': book}
    return render(request, 'books/book_detail.html', data)

def book_create(request):
    form = BookForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('books:book_list')
    return render(request, 'books/book_form.html', {'form': form, 'new_or_edit': 'New'})

    ## using forms manually method
    # if request.POST:
    #     try:
    #         book = Book()
    #         book.title = request.POST["title"]
    #         book.author = request.POST["author"]
    #         book.pages = request.POST["pages"]
    #         book.full_clean()
    #         book.save()
    #         return redirect('books:book_list')
    #     except:
    #         return HttpResponse("You encountered an error!!")

    # return render(request, 'books/book_form.html', { 'new_or_edit': 'New'} )

def book_update(request, book_id):
    book = get_book(book_id)
    form = BookForm(request.POST or None, instance = book)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('books:book_list')
    return render(request, 'books/book_form.html', {'form': form, 'new_or_edit': 'Edit'})
    
    ## using forms manually method
    # try:
    #     book = Book.objects.get(pk=book_id)
    
    #     if request.POST:
    #         try:
    #             book.title = request.POST["title"]
    #             book.author = request.POST["author"]
    #             book.pages = request.POST["pages"]
    #             book.full_clean()
    #             book.save()
    #             return redirect('books:book_list')
    #         except:
    #             return HttpResponse("You encountered an error!!")

    #     return render(request, 'books/book_form.html', { 'new_or_edit': 'Edit', "book" : book } )
    
    # except:
    #     return HttpResponse("You encountered an error!!!!!!")

def book_delete(request, book_id):
    book = get_book(book_id)
    if request.method=='POST':
        book.delete()
        return redirect('books:book_list')
    return render(request, 'books/book_confirm_delete.html', {'object': book })