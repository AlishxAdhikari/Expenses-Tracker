from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Expense
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .models import ExpCoin
from django.contrib import messages

def hello_world(request):
    return HttpResponse("Hello, world! This is the expenses app.")

def home(request):
         return render(request, 'home.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Expense, ExpCoin

@login_required
def addexpense(request):
    expcoin, created = ExpCoin.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        description = request.POST.get('description')
        category = request.POST.get('category')
        amount_str = request.POST.get('amount')
        date = request.POST.get('date')

        # Convert amount to float and validate
        try:
            amount = float(amount_str)
            if amount <= 0:
                messages.error(request, "Amount must be positive.")
                return redirect('addexpense')
        except (ValueError, TypeError):
            messages.error(request, "Invalid amount entered.")
            return redirect('addexpense')

        # Try to debit the amount from EXP coin balance
        try:
            expcoin.debit(amount)
        except ValueError:
            messages.error(request, "Insufficient EXP coin balance.")
            return redirect('addexpense')

        # Save expense only if debit succeeded
        expense = Expense(
            description=description,
            category=category,
            amount=amount,
            date=date,
            user=request.user
        )
        expense.save()

        messages.success(request, f"Expense of {amount} added and EXP coin debited successfully!")
        return redirect('home')

    context = {
        'expcoin_balance': expcoin.balance
    }
    return render(request, 'add_expense.html', context)


@login_required
def add_money(request):
    expcoin, created = ExpCoin.objects.get_or_create(user=request.user)

    if request.method == "POST":
        amount_str = request.POST.get("amount")
        try:
            amount = float(amount_str)
            if amount <= 0:
                messages.error(request, "Please enter a positive amount.")
                return redirect("add_money")
        except (ValueError, TypeError):
            messages.error(request, "Invalid amount entered.")
            return redirect("add_money")

        expcoin.credit(amount)

        messages.success(request, f"Added {amount} EXP coins successfully!")
        return redirect("home")

    context = {
        'expcoin_balance': expcoin.balance
    }
    return render(request, "add_money.html", context)





def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def logout_view(request):
   
    logout(request)
    return redirect('login')  # Redirect to login page after logout

  # Redirect to home after login

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after registration
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})




