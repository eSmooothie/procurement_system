import logging
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from ..helper import *

logger = logging.getLogger(__name__)


def auth_user(request):
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
    logger.info("at logout_user: user with username {} logout.".format(request.user.username))

    logout(request)
    
    return redirect('login_user')

def login_user(request):

    if 'login_err_msg' in request.session: 
        err_msg = request.session.get('login_err_msg') 
        del request.session['login_err_msg']
    else: 
        err_msg = None

    context = page_context(
        err_msg = err_msg,
    )

    return render(request, template_name='ppmp/login.html', context=context)
