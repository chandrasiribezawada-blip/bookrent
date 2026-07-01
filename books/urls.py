from django.urls import path
from .views import add_book, book_detail, my_books,all_books, owner_dashboard

urlpatterns = [

    path(
        'add-book/',
        add_book,
        name='add_book'
    ),

    path(
        'my-books/',
        my_books,
        name='my_books'
    ),
    path(
    'book/<int:pk>/',
    book_detail,
    name='book_detail'
),
    path(
    'all-books/',
    all_books,
    name='all_books'
),
    path(
    'owner-dashboard/',
    owner_dashboard,
    name='owner_dashboard'
),
]