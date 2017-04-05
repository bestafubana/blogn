from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def signup(request):
    error = ''
    if request.method == 'POST':
        
        if request.POST['password'] == request.POST['password_confirmation']:
            try:
                user = User.objects.get(username=request.POST['username']) #TOTALLY INSECURE
                error = "Username is already taken"
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password']) #TOTALLY INSECURE
                login(request, user)
        else:
            error = "Password and password confirmation don't match"
    return render(request, 'signup.html', {'error': error})    
    
def signin(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            
            if 'next' in request.POST and request.POST['next'] is not None:
                return redirect(request.POST['next'])
            # Redirect to a success page.
            return redirect( '/')
        else:
            return render(request, 'signin.html', {'error': 'Login and/or password are not valid'})   
    else:        
        return render(request, 'signin.html', {'error':error})   
        
def logout_user(request):
    if request.method == 'POST':
        logout(request)
    return redirect('/')