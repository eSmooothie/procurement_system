import logging
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..helper import *
from ..models import CostCenter, CostCenterUser

logger = logging.getLogger("file_log")

# Select Cost Center
@login_required(login_url='login_user')
def index(request):        
    user_cost_centers = CostCenterUser.objects.select_related().filter(user__id=request.user.id)

    if request.path == "/home/ppmp":
        selected_app = "ppmp"
    else:
        selected_app = None

    user_fn = request.user.first_name if request.user.first_name is not None else "No Name"

    context = page_context(
        user_fn = user_fn,
        user_cost_centers=user_cost_centers,
        selected_app=selected_app,
        )

    return render(
        request=request, 
        template_name='ppmp/select_cc.html' if selected_app else 'ppmp/welcome.html', 
        context=context
        )

@login_required(login_url='login_user')
def cc_ppmp(request):
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

