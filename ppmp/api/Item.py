"""
UNDER CONSTRUCTION:

READ ABOUT: DJANGO REST FRAMEWORK
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from ..models import ItemDescription, Prices
from ..serializers import ItemDescriptionSerializer, PriceSerializer

class ItemAPI(APIView):
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if "cat_id" in request.query_params:
            category_id = request.query_params['cat_id']
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        keyword = request.query_params['term'] if "term" in request.query_params else None

        if keyword:
            items = Prices.objects.select_related().filter(item__item__category_id=category_id).filter(
                Q(item__spec_1__icontains=keyword) |
                Q(item__spec_2__icontains=keyword) |
                Q(item__spec_3__icontains=keyword) |
                Q(item__spec_4__icontains=keyword) |
                Q(item__spec_5__icontains=keyword) |
                Q(item__item__general_name__icontains=keyword)
            ).all()
        else:
            items = Prices.objects.select_related().filter(item__item__category_id=category_id).all()

        serialize = PriceSerializer(items, many=True)
        

        data = list()

        for d in serialize.data:

            value = d['item']['item']['general_name']
            if d['item']['spec_1'] != "None":
                value += "-" + d['item']['spec_1']
            if d['item']['spec_2'] != "None":
                value += "-" + d['item']['spec_2']
            if d['item']['spec_3'] != "None":
                value += "-" + d['item']['spec_3']
            if d['item']['spec_4'] != "None":
                value += "-" + d['item']['spec_4']
            if d['item']['spec_5'] != "None":
                value += "-" + d['item']['spec_5']

            formatted_data = {
                'item_id' : d['item']['id'],
                'general_item_id' : d['item']['item']['id'],
                'price' : d['price'],
                'price_id': d['id'],
                'unit' : d['unit'],
                'value' : value,
            }
            data.append(formatted_data)

        return Response(data, status=status.HTTP_200_OK)