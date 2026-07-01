from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm


def home(request):
    return render(request, 'home.html')


def register_owner(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.role = 'OWNER'
            user.save()

            login(request, user)

            return redirect('owner_dashboard')

    else:
        form = RegisterForm()

    return render(
        request,
        'users/register_owner.html',
        {'form': form}
    )


def register_borrower(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.role = 'BORROWER'
            user.save()

            login(request, user)

            return redirect('all_books')

    else:
        form = RegisterForm()

    return render(
        request,
        'users/register_borrower.html',
        {'form': form}
    )