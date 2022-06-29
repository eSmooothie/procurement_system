import logging
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .helper import *
from .models import CostCenter, CostCenterUser

logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
    # check if user is login
    if not has_user(request):
        return redirect("login_user")
        
    user_cost_centers = CostCenterUser.objects.select_related().filter(user__id=request.user.id)

    context = page_context(
        user_fn = request.user.first_name,
        user_cost_centers=user_cost_centers,
        )

    return render(
        request=request, 
        template_name='ppmp/ppmp.html', 
        context=context
        )

def logout_user(request):
    logout(request)
    return redirect('login_user')

def login_user(request):
    context = page_context(err_msg = None)

    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']

        # authenticate user if exist
        user = authenticate(request, username=username, password=password)

        if user is None:
            context['err_msg'] = "Incorrect username or password."

            return render(request, template_name='ppmp/login.html', context=context)

       
        login(request, user) # login user

        return redirect('home')  # redirect to home
    
    
    return render(request, template_name='ppmp/login.html', context=context)
