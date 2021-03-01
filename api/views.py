from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Task
from .serializers import  TaskSerializer


# Create your views here.
@api_view(['GET'])
def apioverview(request):
    api_urls ={
        'list':'/task-list/',
        'Detail View':'/task-detail/<str:pk>',
        'Create': '/task-create/',
        'Update':'/task-update/<str:pk>',
        'Detete': '/task-delete/<str:pk>'
    }
    return Response(api_urls)
@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskdetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def Createtask(request):
    serializer = TaskSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def Updatetask(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=tasks,data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('task deleted successfully')