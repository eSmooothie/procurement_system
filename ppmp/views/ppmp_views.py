import logging
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..helper import *
from ..models import CostCenter, CostCenterUser, Ppmp

logger = logging.getLogger("file_log")

import random

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
def cc_ppmp(request, cc_id):
    # retrieve all request parameter
    request_params = request.GET

    # check if passed cc_id is not empty.
    if cc_id is None:
        # display err msg if cc_id empty
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

    #TODO:query all the ppmp under the selected cost center.
    if "ppmp_year" in request_params:
        selected_year = request_params.get("ppmp_year")
        
    else:
        # retrieve the latest year among ppmp data under selected cost center
        selected_year = '2022'
    
    ppmp_year = []
    # retrieve all years in ppmp
    year_in_ppmp = Ppmp.objects.only('year').distinct('year').order_by('-year')

    for year in year_in_ppmp:
        ppmp_year.append(year.year)

    # get only the ppmp based on the selected year
    ppmp_list = Ppmp.objects.filter(cc_id=cc_id,year=selected_year).all

    print(ppmp_list)

    context = page_context(
        user_fn = request.user.first_name,
        cost_center_data=cost_center_data,
        ppmp_year = ppmp_year,
        selected_year = selected_year,
        cc_ppmp_list = ppmp_list,
        selected_app="ppmp",
        )

    return render(
        request=request, 
        template_name='ppmp/cc_ppmp.html', 
        context=context
        )

