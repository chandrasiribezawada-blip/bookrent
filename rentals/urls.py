from django.urls import path
from .views import (
    request_book,
    owner_requests,
    approve_request,
    reject_request,
    borrowed_books,
    return_book
)

urlpatterns = [
    path(
        'borrowed-books/',
        borrowed_books,
        name='borrowed_books'
    ),

    path(
        'return-book/<int:request_id>/',
        return_book,
        name='return_book'
    ),

    path(
        'request-book/<int:book_id>/',
        request_book,
        name='request_book'
    ),

    path(
        'owner-requests/',
        owner_requests,
        name='owner_requests'
    ),

    path(
        'approve/<int:request_id>/',
        approve_request,
        name='approve_request'
    ),

    path(
        'reject/<int:request_id>/',
        reject_request,
        name='reject_request'
    ),
]