"""
UNDER CONSTRUCTION:

READ ABOUT: DJANGO REST FRAMEWORK
"""
import re
from unicodedata import category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from ..models import CostCenter, CostCenterBudget, OrderDetails
from ..serializers import CCBudgetSerializer, CostCenterSerializer, OrderDetailsSerializer

class CostCenterPPMPDetails(APIView):
    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        if ("cat_id" not in request.query_params or 
        "cc_id" not in request.query_params or 
        "sof_id" not in request.query_params or 
        "ppmp_id" not in request.query_params):
            return Response({
                "details" : "Missing query parameters."
            }, status=status.HTTP_200_OK)

        cat_id = request.query_params.get('cat_id')
        cc_id = request.query_params.get('cc_id')
        sof_id = request.query_params.get('sof_id')
        ppmp_id = request.query_params.get('ppmp_id')

        #TODO: Query all ppmp data related to 
        data = dict()
        cost_center = CostCenter.objects.get(id=cc_id)
        cost_center_serializer = CostCenterSerializer(cost_center)
        data['cost_center'] = cost_center_serializer.data

        # get cc budget
        cc_budget = CostCenterBudget.objects.select_related().filter(cc_id=cc_id).filter(category_id=cat_id).all()
        cc_budget_serializer = CCBudgetSerializer(cc_budget, many=True)
        data['budget'] = cc_budget_serializer.data

        orderdetails = OrderDetails.objects.select_related().filter(ppmp_id=ppmp_id).filter(item_desc__item__category_id=cat_id).all()
        orderdetails_serializer = OrderDetailsSerializer(orderdetails, many=True)
        data['order_details'] = orderdetails_serializer.data

        return Response(data, status=status.HTTP_200_OK)