from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import FunnelStatus, Student, Log
from .serializers import FunnelStatusSerializer, StudentSerializer, LogSerializer

#api endpoint for getting list of all the funnel status
@api_view(['GET'])
def get_funnel_status_list(request):

    #get all status
    #serialize them
    #return json
    statuses = FunnelStatus.objects.all()
    serializer = FunnelStatusSerializer(statuses, many=True)
    return JsonResponse({'statuses': serializer.data})


