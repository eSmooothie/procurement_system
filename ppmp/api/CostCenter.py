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
from ..models import CostCenter, CostCenterBudget
from ..serializers import CCBudgetSerializer

class CostCenterPPMPDetails(APIView):
    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        print(request.query_params)

        if "cat_id" not in request.query_params or "cc_id" not in request.query_params or "sof_id" not in request.query_params or "ppmp_id" not in request.query_params:
            return Response({
                "detail" : "Missing query parameters."
            }, status=status.HTTP_200_OK)

        cat_id = request.query_params.get('cat_id')
        cc_id = request.query_params.get('cc_id')
        sof_id = request.query_params.get('sof_id')
        ppmp_id = request.query_params.get('ppmp_id')

        #TODO: Query all ppmp data related to 
        
        cc_budget = CostCenterBudget.objects.select_related().filter(cc_id=cc_id).filter(category_id=cat_id).first()
        cost_center = cc_budget.cc
        
        

        return Response([], status=status.HTTP_200_OK)