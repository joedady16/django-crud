from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm, CreateCustomerForm, UpdateCustomerForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Customer

from django.contrib import messages

# Home page
def home(request):

    return render(request, 'webapp/index.html')


# Register
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")

            return redirect('my-login')
    
    context = {'form': form}

    return render(request, 'webapp/register.html', context=context)

# Login a user

def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect('dashboard')

    context = {'form':form}

    return render(request, 'webapp/my-login.html', context=context)


# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):

    my_records = Customer.objects.all()

    context = {'customers': my_records}

    return render(request, 'webapp/dashboard.html', context=context)

# Create a Customer
@login_required(login_url='my_login')
def create_customer(request):

    form = CreateCustomerForm()

    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer created successfully!")
            return redirect("dashboard")
    
    context = {'form': form}
    return render(request, 'webapp/create-customer.html', context=context)

# Update a customer

@login_required(login_url='my_login')
def update_customer(request, pk):

    customer = Customer.objects.get(id=pk)

    form = UpdateCustomerForm(instance=customer)
    if request.method == 'POST':
        form = UpdateCustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            messages.success(request, "Customer updated successfully!")
            return redirect("dashboard")
        
    context = {'form': form}
    return render(request, 'webapp/update-customer.html', context=context)

# View a singular customer

@login_required(login_url='my_login')
def singular_customer(request, pk):

    all_customers = Customer.objects.get(id=pk)
    context = {'customer': all_customers}
    return render(request, 'webapp/view-customer.html', context=context)



#delete a customer record
@login_required(login_url='my_login')
def delete_customer(request, pk):
    
    customer = Customer.objects.get(id=pk)
    customer.delete()
    messages.success(request, "Customer deleted successfully!")
    return redirect('dashboard')

# - User Logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logged out!")

    return redirect('my-login')