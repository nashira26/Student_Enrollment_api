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
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def funnel_status(request, id):

    #get the status object if exists
    try:
        status = FunnelStatus.objects.get(pk=id)
    except FunnelStatus.DoesNotExist:
        return JsonResponse(
                {"error": "Resource not found", 
                 "message" : "The requested Funnel Status does not exist."}, 
                status=404)
    serializer = FunnelStatusSerializer(status)

    #api endpoint for getting funnel status
    if request.method == "GET":
        return JsonResponse(serializer.data, status=201)
    
    #api endpoint for updating existing funnel status
    elif request.method == "PUT":
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    #api endpoint for deleting an existing funnel status
    elif request.method == "DELETE":
        status.delete()
        return JsonResponse({}, status=204)

#api endpoint for creating a new student
@api_view(['POST'])
def create_student(request):

    #get new student data
    #if valid, save and return response with status
    #else return error message
    first_status = FunnelStatus.objects.first()
    request.data['status'] = first_status

    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT'])
def student(request, id):

    #get the student object if exists
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return JsonResponse(
                {"error": "Resource not found", 
                 "message" : "The requested student does not exist."}, 
                status=404 )
    
    #api endpoint for getting student
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data, status=201)
    
    #api endpoint for updating student
    elif request.method == "PUT":
        status_before=student.status

        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data

            new_status = validated_data.get('status')
            new_name = validated_data.get('name')

            # update in the student object
            student.status = new_status
            student.name = new_name
            student.save()

            #create a log entry for the update
            log_entry = Log(student_name=student, status_before=status_before, status_after=student.status)
            log_entry.save()
        
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)

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
    return JsonResponse(serializer.data, safe=False)
