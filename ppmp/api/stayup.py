from django.http import JsonResponse
from rest_framework import status


def awake(request):

    msg="I'm awake"

    return JsonResponse(data={'msg':msg}, status=status.HTTP_200_OK)