from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.core.paginator import Paginator
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

#api endpoint for creating a new student
@api_view(['POST'])
def create_student(request):

    #get new student data
    #if valid, save and return response with status
    #else return error message
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        #create log entry for new student creation
        student = serializer.instance
        log_entry = Log(student, name=student, status_before=None, status_after=student.status)
        log_entry.save()
        
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

#api endpoint for getting student
@api_view(['GET'])
def get_student(request, id):

    #get the student object if exists
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response(status=404)
    serializer = StudentSerializer(student)
    return Response(serializer.data, status=201)
    

#api endpoint for updating existing student
@api_view(['PUT'])
def update_student(request, id):

    #get existing student object
    #deserialize request data
    #update student object with deserialized data
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=404)
    
    status_before=student.status
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        updated_student = serializer.save()

        #create a log entry for the update
        log_entry = Log(student_name=updated_student, status_before=status_before, status_after=updated_student.status)
        log_entry.save()
        
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

#api endpoint for getting latest 50 logs
@api_view(['GET'])
def get_latest_logs(request):

    #get latest 50 logs
    logs = Log.objects.all().order_by('-timestamp')[:50]
    # paginate logs, 25 logs per page
    paginator = Paginator(logs, 25)
    page_no = request.query_params.get('page', 1)
    page = paginator.get_page(page_no)
    serializer = LogSerializer(page, many=True)
    return Response(serializer.data)
