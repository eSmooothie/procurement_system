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

    s_sof = request.GET['f_sof'] if 'f_sof' in request.GET else sof[0].code
    s_year = request.GET['f_year'] if 'f_year' in request.GET else ppmp_year[0]
    is_unconsolidate = 'f_unconsolidated' in request.GET 
    is_primary = 'f_primary' in request.GET
    is_supplementary = 'f_sup' in request.GET
    cat_name = request.GET['search_category'] if 'search_category' in request.GET else ""
    cat_code = re.search('\((.+)\)', cat_name).groups()[0] if cat_name != "" else None

    filter = [
        Q(orderdetail__ppmp__sof__code = s_sof),
        Q(orderdetail__ppmp__year = s_year)
    ]
    print("U:{} P:{} S:{}".format(is_unconsolidate, is_primary, is_supplementary))

    if is_unconsolidate and not is_primary and not is_supplementary: #TFF
        filter.append(Q(mode__isnull=True))
    elif is_unconsolidate and is_primary and not is_supplementary: #TTF
        filter.append(Q(mode__isnull=True) | Q(mode='primary'))
    elif is_unconsolidate and not is_primary and is_supplementary: #TFT
        filter.append(Q(mode__isnull=True) | Q(mode='supplementary'))
    elif not is_unconsolidate and is_primary and is_supplementary: #FTT
        filter.append(Q(mode__isnull=False))
    elif not is_unconsolidate and not is_primary and is_supplementary: #FFT
        filter.append(Q(mode='supplementary'))
    elif not is_unconsolidate and is_primary and not is_supplementary: #FTF
        filter.append(Q(mode='primary'))

    if cat_code is not None:
        filter.append(Q(orderdetail__cat_code=cat_code))

    items = ProcurementMode.objects.select_related().filter(*filter).all()

    print(items)

    context = page_context(
        user_fn = user_fn,
        is_admin=is_admin,
        selected_app=selected_app,
        items=items,

        sof=sof,
        ppmp_year=ppmp_year,
    )

    return render(
        request=request, 
        template_name='app/select_app.html' if selected_app else 'ppmp/welcome.html', 
        context=context
     )
