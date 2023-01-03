import logging
from unicodedata import category
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ppmp.serializers import OrderDetailsSerializer

from ..helper import *
from ..models import Category, CostCenter, CostCenterBudget, CostCenterUser, OrderDetails, Ppmp, Prices, SourceOfFund

logger = logging.getLogger("file_log")

from babel.numbers import format_currency
from datetime import date

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
        is_admin = request.user.is_staff,
        user_cost_centers=user_cost_centers,
        selected_app=selected_app,
        )

    return render(
        request=request, 
        template_name='ppmp/select_cc.html', 
        context=context
        )

@login_required(login_url='login_user')
def dashboard(request):
    user_fn = request.user.first_name if request.user.first_name is not None else "No Name"
    is_admin = request.user.is_staff

    if not is_admin:
        user_cc = CostCenterUser.objects.select_related().filter(user_id = request.user.id).values('cc__code')
        ppmps = Ppmp.objects.select_related().filter(cc_code__in=user_cc).values('id')
        orderdetails = OrderDetails.objects.select_related().filter(ppmp_id__in=ppmps).order_by('cat_code', '-ppmp__year').distinct('cat_code')
        
    else:
        ppmps = Ppmp.objects.select_related().all()
        orderdetails = OrderDetails.objects.select_related().filter(ppmp_id__in=ppmps).order_by('cat_code', '-ppmp__year').distinct('cat_code')

    my_orderdetails = []

    for order in orderdetails:
        data = {
            'id' : order.id,
            'ppmp' : order.ppmp,
            'cc' : CostCenter.objects.get(code=order.ppmp.cc_code),
            'cat' : Category.objects.get(code=order.cat_code),
            'sof' : order.ppmp.sof,
        }
        my_orderdetails.append(data)

    context = page_context(
        user_fn = user_fn,
        selected_app="dashboard",
        is_admin=is_admin,
        orderdetails = my_orderdetails,
    )

    return render(
        request=request, 
        template_name='ppmp/welcome.html', 
        context=context
    )

@login_required(login_url='login_user')
def cc_ppmp(request, cc_code):
    # retrieve all request parameter
    request_params = request.GET

    # check if passed cc_id is not empty.
    if cc_code is None:
        # display err msg if cc_id empty
        logger.error("user_id#{}: at cc_ppmp: cc_id is empty.".format(request.user.id))
        return redirect("ppmp")
    
    # check if cost center exist in db.
    if not CostCenter.objects.select_related().filter(code=cc_code).exists():
        logger.info("user_id#{}: at cc_ppmp: cost center id#{} does not exist in database.".format(request.user.id, cc_code))
        return redirect("ppmp")

    # check if user is allowed to access the cost center.
    if not CostCenterUser.objects.select_related().filter(user__id=request.user.id).filter(cc__code=cc_code).exists():
        logger.warning("user_id#{}: at cc_ppmp: user is not allowed to access cc_id#{}".format(request.user.id, cc_code))
        return redirect("ppmp")
    
    cost_center_data = CostCenterUser.objects.filter(user__id=request.user.id).get(cc__code=cc_code).cc    

    ppmp_year = list()
    # retrieve all years in cc's ppmp
    year_in_ppmp = Ppmp.objects.distinct('year').filter(cc_code=cost_center_data.code).order_by('-year')

    for year in year_in_ppmp:
        ppmp_year.append(year.year)

    if not ppmp_year:
        todays_date = date.today()
        ppmp_year.append(todays_date.year)

    selected_year = request_params.get("year") if "year" in request_params else ppmp_year[0]

    # get only the ppmp based on the selected year
    ppmp_list = Ppmp.objects.filter(cc_code=cc_code,year=selected_year).all()

    # form
    # curr_year + 1 and curr_year
    form_year_opt = [int(ppmp_year[0])+1, int(ppmp_year[0])]
    form_sof_opt = SourceOfFund.objects.all()
    form_type_opt = ['PRIMARY','SUPLEMENTARY']

    context = page_context(
        user_fn = request.user.first_name,
        is_admin = request.user.is_staff,
        cost_center_data=cost_center_data,
        ppmp_year = ppmp_year,
        selected_year = selected_year,
        cc_ppmp_list = ppmp_list,
        selected_app="ppmp",
        form_year_opt=form_year_opt,
        form_sof_opt=form_sof_opt,
        form_type_opt=form_type_opt
    )

    return render(
        request=request, 
        template_name='ppmp/cc_ppmp.html', 
        context=context
    )


@login_required(login_url='login_user')
def ppmp_detail(request, ppmp_id):

    cat_code = request.GET['category_selected'] if 'category_selected' in request.GET else None

    ppmp = Ppmp.objects.get(id=ppmp_id)
    cc = CostCenter.objects.get(code=ppmp.cc_code)

    category = Category.objects.filter(code=cat_code).get() if cat_code else None
    raw_orderdetails = OrderDetails.objects.filter(cat_code=cat_code, ppmp__id = ppmp.id).all() if cat_code else None

    cc_budget = None
    if cat_code and CostCenterBudget.objects.select_related().filter(cc__code=cc.code, cat__code=cat_code).order_by('-id').exists():
        cc_budget = CostCenterBudget.objects.select_related().filter(cc__code=cc.code, cat__code=cat_code).order_by('-id').get()

    curr_budget = format_currency(cc_budget.curr_budget, 'PHP', locale="en_US") if cc_budget else "NO BUDGET"

    orderdetails = list()
  
    if raw_orderdetails:
        for data in raw_orderdetails:
            id = data.id
            item_id = data.item.id
            item_name = data.item.name
            item_unit = data.item.unit
            item_price = float(data.item.get_price(datetime=datetime.date(year=int(ppmp.year), month=1, day=1)))
            first_q = (data.first_quant, format_currency(round(float(data.first_quant) * item_price, 2), 'PHP', locale="en_US") )
            second_q = (data.second_quant, format_currency(round(float(data.second_quant) * item_price, 2), 'PHP', locale="en_US") )
            third_q = (data.third_quant, format_currency(round(float(data.third_quant) * item_price, 2), 'PHP', locale='en_US') )
            fourth_q = (data.fourth_quant, format_currency(round(float(data.fourth_quant) * item_price, 2), 'PHP', locale='en_US') )

            item_price = format_currency(item_price, "PHP", locale='en_US')

            pr = data.purchase_request

            orderdetails.append({
                'id' : id,
                'item_id' : item_id,
                'item_name' : item_name,
                'item_unit' : item_unit,
                'item_price' : item_price,
                'first_quart' : first_q,
                'second_quart' : second_q,
                'third_quart' : third_q,
                'fourth_quart' : fourth_q,
                'pr' : pr,
            })

    context = page_context(
        user_fn = request.user.first_name,
        is_admin = request.user.is_staff,
        ppmp=ppmp,
        cc=cc,
        curr_budget=curr_budget,
        category=category,
        orderdetails=orderdetails,
    )

    return render(
        request=request, 
        template_name='ppmp/ppmp_details.html', 
        context=context
    )

@login_required(login_url='login_user')
def ppmp_admin(request):
    pass

@login_required(login_url='login_user')
def view_logs(request, ppmp_id, cat_code):

    ppmp = Ppmp.objects.get(id=ppmp_id)
    cc = CostCenter.objects.get(code=ppmp.cc_code)

    category = Category.objects.filter(code=cat_code).get() if cat_code else None
    raw_orderdetails = OrderDetails.objects.filter(cat_code=cat_code, ppmp__id = ppmp.id).all() if cat_code else None

    cc_budget = None
    if cat_code and CostCenterBudget.objects.select_related().filter(cc__code=cc.code, cat__code=cat_code).order_by('-id').exists():
        cc_budget = CostCenterBudget.objects.select_related().filter(cc__code=cc.code, cat__code=cat_code).order_by('-id').get()

    curr_budget = format_currency(cc_budget.curr_budget, 'PHP', locale="en_US") if cc_budget else "NO BUDGET"

    orderdetails = list()
    if raw_orderdetails:
        for data in raw_orderdetails:
            id = data.id
            item_id = data.item.id
            item_name = data.item.name
            item_unit = data.item.unit
            app_status = data.app_status
            rq_status = data.received_quotation_status
            awb_status = data.award_winning_bidder_status
            oblpo_status = data.obligate_po_status
            serv_status = data.served_status

            orderdetails.append({
                'id' : id,
                'item_id' : item_id,
                'item_name' : item_name,
                'item_unit' : item_unit,
                'app_status' : app_status,
                'rq_status' : rq_status,
                'awb_status' : awb_status,
                'oblpo_status' : oblpo_status,
                'serv_status' : serv_status
            })

    context = page_context(
        user_fn = request.user.first_name,
        is_admin = request.user.is_staff,
        ppmp=ppmp,
        cc=cc,
        curr_budget=curr_budget,
        category=category,
        orderdetails=orderdetails,
    )

    return render(
        request=request, 
        template_name='ppmp/view_log.html', 
        context=context
    )

@login_required(login_url='login_user')
def view_pr(request, ppmp_id, cat_code, orderitem_id):
    user_cost_centers = CostCenterUser.objects.select_related().filter(user__id=request.user.id)
    user_fn = request.user.first_name if request.user.first_name is not None else "No Name"

    order_detail = OrderDetails.objects.get(id=orderitem_id)

    context = page_context(
        user_fn = user_fn,
        is_admin = request.user.is_staff,
        user_cost_centers=user_cost_centers,
        order_detail=order_detail,
    )

    return render(
        request=request, 
        template_name='ppmp/purchase_req.html', 
        context=context
    )
#############

