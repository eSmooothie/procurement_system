import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from rest_framework import status

from ..models import Ppmp, SourceOfFund
INVALID_REQUEST = {'msg':"Invalid request"}
INVALID_ACCESS = {'msg':"Invalid access"}

def add_ppmp(request):

    if request.method == "POST":
        if 'year' not in request.POST or 'sof' not in request.POST or 'type' not in request.POST or 'cc_code' not in request.POST:
            messages.error(request, 'FAIL: Missing parameters.')
            return JsonResponse(INVALID_REQUEST, status=status.HTTP_400_BAD_REQUEST)

        sof = SourceOfFund.objects.get(id=request.POST['sof'])
        year = request.POST['year']
        cc_code = request.POST['cc_code']
        type = request.POST['type']

        if type == 'PRIMARY' and Ppmp.objects.filter(sof=sof, year=year, type=type, cc_code=cc_code).exists():
            messages.error(request, 'FAIL: Only one Primary is allowed for every cost center per source of fund.')
            return JsonResponse({'msg':'FAIL: Only one Primary is allowed for every cost center per source of fund.'}, status=status.HTTP_202_ACCEPTED)

        new_ppmp = Ppmp()
        
        new_ppmp.cc_code = cc_code
        new_ppmp.sof = sof
        new_ppmp.year = year
        new_ppmp.type = type

        new_ppmp.save()

        data = {"message":"created"}
        # messages.success(request, 'Success')
        return JsonResponse(data, status=status.HTTP_201_CREATED)

    return JsonResponse(INVALID_REQUEST, status=status.HTTP_400_BAD_REQUEST)