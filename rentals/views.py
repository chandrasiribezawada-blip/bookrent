from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required
from django.utils import timezone

from books.models import Book
from .models import RentalRequest


# Borrower requests a book
@login_required
def request_book(request, book_id):

    if request.user.role != 'BORROWER':
        return redirect('all_books')

    book = get_object_or_404(
        Book,
        id=book_id
    )

    # Prevent duplicate pending requests
    existing_request = RentalRequest.objects.filter(
        book=book,
        borrower=request.user,
        status='PENDING'
    ).exists()

    if not existing_request:
        RentalRequest.objects.create(
            book=book,
            borrower=request.user
        )

    return redirect('all_books')


# Owner views requests for their books
@login_required
def owner_requests(request):

    requests = RentalRequest.objects.all()

    return render(
        request,
        'rentals/owner_requests.html',
        {'requests': requests}
    )


# Owner approves request
@login_required
def approve_request(request, request_id):

    rental_request = get_object_or_404(
        RentalRequest,
        id=request_id
    )

    # Security check
    if rental_request.book.owner != request.user:
        return redirect('/')

    rental_request.status = 'APPROVED'

    rental_request.book.is_available = False

    rental_request.book.save()
    rental_request.save()

    return redirect('owner_requests')


# Owner rejects request
@login_required
def reject_request(request, request_id):

    rental_request = get_object_or_404(
        RentalRequest,
        id=request_id
    )

    # Security check
    if rental_request.book.owner != request.user:
        return redirect('/')

    rental_request.status = 'REJECTED'

    rental_request.save()

    return redirect('owner_requests')


# Borrower dashboard
@login_required
def borrowed_books(request):

    rentals = RentalRequest.objects.filter(
        borrower=request.user,
        status='APPROVED'
    )

    return render(
        request,
        'rentals/borrowed_books.html',
        {'rentals': rentals}
    )


# Borrower returns book
@login_required
def return_book(request, request_id):

    rental_request = get_object_or_404(
        RentalRequest,
        id=request_id
    )

    # Security check
    if rental_request.borrower != request.user:
        return redirect('/')

    rental_request.status = 'RETURNED'

    rental_request.return_date = timezone.now().date()

    rental_request.book.is_available = True

    rental_request.book.save()
    rental_request.save()

    return redirect('borrowed_books')