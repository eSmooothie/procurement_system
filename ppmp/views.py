import logging
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .helper import *
from .models import CostCenter, CostCenterUser

logger = logging.getLogger(__name__)
# Select Cost Center
def index(request):
    # check if user is login
    if not has_user(request):
        return redirect("login_user")
        
    user_cost_centers = CostCenterUser.objects.select_related().filter(user__id=request.user.id)

    if request.path == "/home/ppmp":
        selected_app = "ppmp"
    else:
        selected_app = None

    context = page_context(
        user_fn = request.user.first_name,
        user_cost_centers=user_cost_centers,
        selected_app=selected_app,
        )

    return render(
        request=request, 
        template_name='ppmp/select_cc.html' if selected_app else 'ppmp/welcome.html', 
        context=context
        )

# Select 
def cc_ppmp(request):

    # check if user is login
    if not has_user(request):
        return redirect("login_user")
    
    # retrieve all request parameter
    request_params = request.GET

    if not "cc_id" in request_params:
        # display err msg if cc_id not set
        logger.error("user_id#{}: at cc_ppmp: cc_id not set.".format(request.user.id))
        return redirect("ppmp")

    cc_id = request_params.get("cc_id")

    # check if passed cc_id is not empty.
    if cc_id == '':
        logger.error("user_id#{}: at cc_ppmp: cc_id is empty.".format(request.user.id))
        return redirect("ppmp")
    
    # check if cost center exist in db.
    if not CostCenter.objects.select_related().filter(id=cc_id).exists():
        logger.info("user_id#{}: at cc_ppmp: cost center id#{} does not exist in database.".format(request.user.id, cc_id))
        return redirect("ppmp")

    # check if user is allowed to access the cost center.
    if not CostCenterUser.objects.select_related().filter(user__id=request.user.id).filter(cc__id=cc_id).exists():
        logger.warning("user_id#{}: at cc_ppmp: user is not allowed to access cc_id#{}".format(request.user.id, cc_id))
        return redirect("ppmp")
    
    cost_center_data = CostCenterUser.objects.filter(user__id=request.user.id).get(cc__id=cc_id).cc    

    context = page_context(
        user_fn = request.user.first_name,
        cost_center_data=cost_center_data,
        selected_app="ppmp",
        )

    return render(
        request=request, 
        template_name='ppmp/cc_ppmp.html', 
        context=context
        )

def logout_user(request):
    logger.info("at logout_user: user with username {} logout.".format(request.user.username))

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
            logger.info("at login_user: user with username {} attempting to login.".format(username))
            context['err_msg'] = "Incorrect username or password."

            return render(request, template_name='ppmp/login.html', context=context)

       
        login(request, user) # login user
        logger.info("at login_user: user with username {} successfully login.".format(username))
        return redirect('home')  # redirect to home
    
    
    return render(request, template_name='ppmp/login.html', context=context)
