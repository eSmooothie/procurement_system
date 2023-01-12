import json
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from rest_framework import status
from django.contrib import messages

from ppmp.models import App, OrderDetails, ProcurementMode, SourceOfFund
from ppmp.serializers import APPSerializer, OrderDetailsSerializer

INVALID_REQUEST = {'msg':"Invalid request"}
INVALID_ACCESS = {'msg':"Invalid access"}

def get_consolidated_ppmp(request):

    if request.method == "GET":
        req_data = request.GET
        app_type = req_data['type']
        year = req_data['year']
        sof_id = req_data['sof']
        cat_id = req_data['cat_id']
        quarter = parse_quarter(int(req_data['quarter'])) + " QUARTER"
        
        app = App.objects.select_related().filter(
            type=app_type,
            year=year,
            quarter__iexact=quarter,
            source_of_fund__id=sof_id,
            item_desc__item__category__id=cat_id
            ).all()
        
        serialize = APPSerializer(app, many=True)
        raw_data = serialize.data
        print(raw_data)        

        return JsonResponse(raw_data, status=status.HTTP_200_OK)

    return JsonResponse(INVALID_REQUEST, status=status.HTTP_400_BAD_REQUEST)

def parse_quarter(q:int):
    if q == 1:
        return "FIRST"
    elif q == 2:
        return "SECOND"
    elif q == 3:
        return "THIRD"
    elif q == 4:
        return "FOURTH"
    return None

def consolidate_ppmp(request):

    if request.method == "POST":
        raw_data = request.POST
        sof = raw_data['sof']
        year = raw_data['year']
        quarter = raw_data['quarter']
        consolidate_all = True if raw_data['consolidate'] == "1" else False
        
        consolidated_order = ProcurementMode.objects.all().values_list('orderdetail__id')

        query=[
            Q(ppmp__year=year),
            Q(ppmp__sof__code=sof),
        ]

        if not consolidate_all: # specific
            categories = list()

            for cat_code in raw_data.getlist('categories[]'):
                if OrderDetails.objects.select_related().exclude(id__in=consolidated_order).filter(*query, cat_code=cat_code).count() == 0:
                    msg="No item found for account code {} found.".format(cat_code)
                    messages.error(request, msg)
                else:
                    categories.append(cat_code)

            if len(categories) == 0:
                return JsonResponse({"msg":"No APP created"}, status=status.HTTP_201_CREATED, safe=False)

            query.append(
                Q(cat_code__in=categories)
            )

            
        app = App()
        app.quarter=quarter
        app.year=year
        app.sof= SourceOfFund.objects.get(code=sof)
        app.type = "PRIMARY" if not App.objects.filter(sof__code=sof,quarter=quarter,year=year,type="PRIMARY").exists() else "SUPLEMENTARY"
        app.save()

        orderdetails = OrderDetails.objects.select_related().exclude(id__in=consolidated_order).filter(*query).all()
        
        for order in orderdetails:
            procure_mode = ProcurementMode()
            procure_mode.app = app
            procure_mode.orderdetail = order
            procure_mode.mode = app.type
            procure_mode.save()

        return JsonResponse({"msg":"OK"}, status=status.HTTP_201_CREATED, safe=False)

    return JsonResponse(INVALID_REQUEST, status=status.HTTP_400_BAD_REQUEST)