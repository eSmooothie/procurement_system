import logging
from unicodedata import category
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..helper import *
from ..models import App, Category, CostCenter, CostCenterBudget, CostCenterUser, OrderDetails, Ppmp, SourceOfFund

logger = logging.getLogger("file_log")

from babel.numbers import format_currency
from datetime import date

selected_app = "app"
# Select Cost Center
@login_required(login_url='login_user')
def index(request):        

    user_fn = request.user.first_name if request.user.first_name is not None else "No Name"

    sof = SourceOfFund.objects.all().order_by('-id')

    distinct_app_year = App.objects.order_by('-year').distinct('year').values('year')

    distinct_app_type = App.objects.order_by('-type').distinct('type').values('type')

    print(distinct_app_year)
    context = page_context(
        user_fn = user_fn,
        selected_app=selected_app,
        sof=sof,
        distinct_app_year=distinct_app_year,
        distinct_app_type=distinct_app_type
    )

    return render(
        request=request, 
        template_name='app/select_app.html' if selected_app else 'ppmp/welcome.html', 
        context=context
     )