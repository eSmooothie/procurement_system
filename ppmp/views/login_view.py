import logging
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from ..helper import *

logger = logging.getLogger("file_log")


def auth_user(request):
    '''Authenticate user by checking the inputted username and password. The request method should be POST.'''
    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']

        # authenticate user if exist
        user = authenticate(request, username=username, password=password)

        if user is None:
            logger.info("at login_user: user with username '{}' attempting to login.".format(username))
            request.session['login_err_msg'] = "Incorrect username or password."

            return redirect('login_user')

       
        login(request, user) # login user
        logger.info("at login_user: user with username '{}' successfully login.".format(username))
        return redirect('home')  # redirect to home
    else:
        return redirect('login_user')

def logout_user(request):
    '''Logout user.'''
    logger.info("at logout_user: user with username {} logout.".format(request.user.username))

    logout(request)
    
    return redirect('login_user')

def login_user(request):
    '''login user interface.'''
    if 'login_err_msg' in request.session: 
        err_msg = request.session.get('login_err_msg') 
        del request.session['login_err_msg'] # delete session after instantiated
    else: 
        err_msg = None

    # check if user is already login
    if request.user.is_authenticated:
        return redirect('home')
        

    context = page_context(
        err_msg = err_msg,
    )

    return render(request, template_name='ppmp/login.html', context=context)
