import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import status

from ppmp.models import App
from ppmp.serializers import APPSerializer

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