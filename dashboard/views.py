from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from users.models import User
from books.models import Book
from rentals.models import RentalRequest


@login_required
def admin_dashboard(request):

    if request.user.role != 'ADMIN':
        return render(request, '403.html')

    context = {

        'total_users':
        User.objects.count(),

        'total_owners':
        User.objects.filter(
            role='OWNER'
        ).count(),

        'total_borrowers':
        User.objects.filter(
            role='BORROWER'
        ).count(),

        'total_books':
        Book.objects.count(),

        'pending_requests':
        RentalRequest.objects.filter(
            status='PENDING'
        ).count(),

        'approved_requests':
        RentalRequest.objects.filter(
            status='APPROVED'
        ).count(),

        'returned_books':
        RentalRequest.objects.filter(
            status='RETURNED'
        ).count(),
    }

    return render(
        request,
        'dashboard/admin_dashboard.html',
        context
    )