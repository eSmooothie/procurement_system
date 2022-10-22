import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import status

INVALID_REQUEST = {'msg':"Invalid request"}
INVALID_ACCESS = {'msg':"Invalid access"}

def get_consolidated_ppmp(request):

    if request.method == "GET":
        req_data = request.GET
        return JsonResponse(req_data, status=status.HTTP_200_OK)

    return JsonResponse(INVALID_REQUEST, status=status.HTTP_400_BAD_REQUEST)