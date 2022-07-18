"""
UNDER CONSTRUCTION:

READ ABOUT: DJANGO REST FRAMEWORK
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from ..models import Ppmp
from ..serializers import PpmpSerializer

class PpmpListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all the ppmp items for given requested user
        '''
        params = request.query_params
        # ppmps = Ppmp.objects.filter(user = request.user.id)
        # serializer = PpmpSerializer(ppmps, many=True)
        return Response(params, status=status.HTTP_200_OK)


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Ppmp with given ppmp data
        '''
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }

        serializer = PpmpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)