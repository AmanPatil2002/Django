# ...existing code...
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def index(request):
    # redirect anonymous users to login
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            auth_login(request, user)
            return redirect('index')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('/login')
# ...existing code...