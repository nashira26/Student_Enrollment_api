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

#api endpoint for creating a new funnel status
@api_view(['POST'])
def create_funnel_status(request):

    #get new status data
    #if valid, save and return response with status
    #else return error message
    serializer = FunnelStatusSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

#api endpoint for getting funnel status
@api_view(['GET'])
def get_funnel_status(request, id):

    #get the status object if exists
    try:
        status = FunnelStatus.objects.get(pk=id)
    except FunnelStatus.DoesNotExist:
        return Response(status=404)
    serializer = FunnelStatusSerializer(status)
    return Response(serializer.data, status=201)
    
#api endpoint for updating existing funnel status
@api_view(['PUT'])
def update_funnel_status(request, id):

    #get existing funnel status object
    #deserialize request data
    #update funnel status object with deserialized data
    try:
        status = FunnelStatus.objects.get(pk=id)
    except FunnelStatus.DoesNotExist:
        return Response(status=404)
    serializer = FunnelStatusSerializer(status, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

#api endpoint for deleting an existing funnel status
@api_view(['DELETE'])
def delete_funnel_status(request, id):

    #get the status object
    #delete it
    #return status
    try:
        status = FunnelStatus.objects.get(id=id)
    except FunnelStatus.DoesNotExist:
        return Response(status=404)
    status.delete()
    return Response(status=204)

