import logging
from unicodedata import category
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import Q
import re

from ..helper import *
from ..models import App, Category, CostCenter, CostCenterBudget, CostCenterUser, OrderDetails, Ppmp, ProcurementMode, SourceOfFund

logger = logging.getLogger("file_log")

from babel.numbers import format_currency
from datetime import date

selected_app = "app"
# Select Cost Center
@login_required(login_url='login_user')
def index(request):        

    user_fn = request.user.first_name if request.user.first_name is not None else "No Name"
    is_admin = request.user.is_staff

    sof = SourceOfFund.objects.all()
    ppmp_year = Ppmp.objects.all().distinct('year').order_by('-year').values_list('year')


    items = ProcurementMode.objects.all().distinct('orderdetail__cat_code')
    apps = list()

    for i in items:
        data = {}
        data['ttl_enduser'] = ProcurementMode.objects.filter(app=i.app, orderdetail__cat_code=i.orderdetail.cat_code).distinct('orderdetail__ppmp__cc_code').count()
        data['item'] = i
        apps.append(data)
    
    context = page_context(
        user_fn = user_fn,
        is_admin=is_admin,
        selected_app=selected_app,
        items=apps,

        sof=sof,
        ppmp_year=ppmp_year,
    )

    return render(
        request=request, 
        template_name='app/select_app.html' if selected_app else 'ppmp/welcome.html', 
        context=context
     )