from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm


@login_required
def add_book(request):

    if request.user.role != 'OWNER':
        return redirect('/')

    if request.method == 'POST':

        form = BookForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            book = form.save(commit=False)

            book.owner = request.user

            book.save()

            return redirect('/my-books/')

    else:

        form = BookForm()

    return render(
        request,
        'books/add_book.html',
        {'form': form}
    )


@login_required
def my_books(request):

    books = Book.objects.filter(
        owner=request.user
    )

    return render(
        request,
        'books/my_books.html',
        {'books': books}
    )
from django.shortcuts import get_object_or_404

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, id=pk)

    return render(
        request,
        'books/book_detail.html',
        {'book': book}
    )
    
@login_required
def edit_book(request, pk):

    book = get_object_or_404(
        Book,
        id=pk,
        owner=request.user
    )

    if request.method == 'POST':

        form = BookForm(
            request.POST,
            request.FILES,
            instance=book
        )

        if form.is_valid():
            form.save()
            return redirect('my_books')

    else:
        form = BookForm(instance=book)

    return render(
        request,
        'books/edit_book.html',
        {'form': form}
    )
    
@login_required
def delete_book(request, pk):

    book = get_object_or_404(
        Book,
        id=pk,
        owner=request.user
    )

    book.delete()

    return redirect('my_books')



from django.db.models import Q

@login_required
def all_books(request):

    books = Book.objects.filter(
        is_available=True
    )

    search = request.GET.get('search')

    if search:
        books = books.filter(
            Q(title__icontains=search) |
            Q(author__icontains=search) |
            Q(category__icontains=search)
        )

    return render(
        request,
        'books/all_books.html',
        {'books': books}
    )
    
    
from rentals.models import RentalRequest
from django.contrib.auth.decorators import login_required


@login_required
def owner_dashboard(request):

    if request.user.role != 'OWNER':
        return redirect('/')

    total_books = Book.objects.filter(
        owner=request.user
    ).count()

    available_books = Book.objects.filter(
        owner=request.user,
        is_available=True
    ).count()

    pending_requests = RentalRequest.objects.filter(
        book__owner=request.user,
        status='PENDING'
    ).count()

    approved_requests = RentalRequest.objects.filter(
        book__owner=request.user,
        status='APPROVED'
    ).count()

    context = {
        'total_books': total_books,
        'available_books': available_books,
        'pending_requests': pending_requests,
        'approved_requests': approved_requests,
    }

    return render(
        request,
        'books/owner_dashboard.html',
        context
    )