from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.template.context_processors import csrf
from .models import Member
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password


# Corrected view function
def registrations(request):
    msg = None  # Initialize msg to None

    if request.method == 'POST':
        # Retrieve form data
        username1 = request.POST.get('username')
        email1 = request.POST.get('email')
        password1 = request.POST.get('password')
        rePassword1 = request.POST.get('re-enterPassword')

        # Check if passwords match
        if password1 == rePassword1:
            # Create a new Member and save it to the database
            member = Member(username=username1, email=email1, password=make_password(password1))
            member.save()
            msg = True
        else:
            msg = False

    # Pass the message to the context
    context = {'message': msg}

    # Render the template with the context and return the response
    return render(request, 'registration.html', context)


def login(request):
    # template = loader.get_template('login.html')
    msg = None
    context = {'csrf_token': csrf(request)['csrf_token'],}
    if request.method == 'POST':
        userLogin = request.POST.get('username')
        passLogin = request.POST.get('pass')

        check_user = Member.objects.get(username=userLogin)
        # Check if the hashed password matches
        if check_password(passLogin, check_user.password):
            request.session['user'] = userLogin
            msg = True
            return redirect('/profile', msg)
            
        else:
            msg = False
            print("Please enter valid username and password")
    context = {
        'message': msg,
    }
    return render(request, 'login.html', context)

       

def profile(request):
    msg = None
    if 'user' in request.session:
        
        username = request.session['user']

        try:
            msg = True
            user = Member.objects.get(username = username)

            context = {
                'userLogin': username,
                'email': user.email,
                'message': msg
            }
            
            template = loader.get_template('profile.html')

            return HttpResponse(template.render(context, request))
        except Member.DoesNotExist:
            return redirect('login/')
    
    else:
        return redirect('login/')
    


def custom_logout(request):
    logout(request)
    return redirect('/')