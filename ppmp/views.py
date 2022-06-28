import logging
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .helper import *
from .forms import LoginForm

logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
    logger.info("TEST FROM INDEX")
    context = page_context(
        test_data="TEST_123",
        )

    return render(
        request=request, 
        template_name='ppmp/home.html', 
        context=context
        )

def logout_user(request):
    logout(request)
    return redirect('login_user')

def login_user(request):
    context = page_context(err_msg = None)
    
    logger.warning("TEST LOGIN")

    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']

        # authenticate user if exist
        user = authenticate(request, username=username, password=password)

        if user is None:
            context['err_msg'] = "Incorrect username or password."

            return render(request, template_name='ppmp/login.html', context=context)

        # redirect to home
        login(request, user)

        return redirect('home')
    
    
    return render(request, template_name='ppmp/login.html', context=context)
