from django.shortcuts import render, redirect
#from .models import Employee

# Show Login page

def login_form(request):
    if request.method == "POST":
        return redirect('/login/dashboard')
    else:
        return render(request, 'login-form.html')

def login_show(request):
    return render(request, 'login-show.html')