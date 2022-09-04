"""
UNDER CONSTRUCTION:

READ ABOUT: DJANGO REST FRAMEWORK
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from ..models import Category
from ..serializers import CategorySerializer

class CategoryAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        keyword = request.query_params['term'] if "term" in request.query_params else None

        if keyword:
            categories = Category.objects.filter(name__icontains=keyword)
        else:
            categories = Category.objects.all()

        serialize = CategorySerializer(categories, many=True)
        

        data = list()

        for d in serialize.data:
            formatted_data = {
                'id' : d['id'],
                'code' : d['code'],
                'value' : f"{d['name']} ({d['code']})",
            }

            data.append(formatted_data)

        
        return Response(data, status=status.HTTP_200_OK)