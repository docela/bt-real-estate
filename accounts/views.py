from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.


def register(request):
    if request.method == "POST":
        # This gets the form values.
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # This checks if passwords match.
        if password == password2:
            # This check the username to see if it already exists in our database. We don't want duplicates.
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken.')
                return redirect('register')
            else:
                # If the username doesn't exist, we then need to check the email hasn't already been used.
                if User.objects.filter(email=email).exists():
                    messages.error(
                        request, 'This email is already being used.')
                    return redirect('register')
                else:
                    # If both passes then we can register our user.
                    user = User.objects.create_user(
                        first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                    user.save()
                    messages.success(
                        request, 'You are now registered and can log in.')
                    return redirect('login')
        else:
            messages.error(
                request, "Passwords do not match. Please try again.")
            return redirect('register')
    # This gets the register page
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        # If the user is found with the above login details
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    else:
        pass
    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
      auth.logout(request)
      messages.success(request, 'You are now logged out.')
    return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)
