from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status


from App.models import User, Task
from App.serializer import UserSerializer, TaskSerializer

# from django.core.files.storage import default_storage

# def adminApi(request, userId, date, status):


# @csrf_exempt
def adminApi(request):
    # if request.method == 'GET':
    #     tutorials = Tutorial.objects.all()

    #     title = request.query_params.get('title', None)
    #     if title is not None:
    #         tutorials = tutorials.filter(title__icontains=title)

    #     tutorials_serializer = TutorialSerializer(tutorials, many=True)
    #     return JsonResponse(tutorials_serializer.data, safe=False)
    # 'safe=False' for objects serialization
    # print(JSONParser().parse(request))

    if request.method == 'POST':
        task_data = JSONParser().parse(request)
        # print(task_data)
        task_serializer = TaskSerializer(data=task_data)
        # print(task_serializer.errors)
        if task_serializer.is_valid():
            print(task_serializer.validated_data)
            task_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'GET':
        task_data = JSONParser().parse(request)
        tasks = Task.objects.all()

        tasks = tasks.filter(
            userID=task_data['userID'], status=task_data['status'])
        # print(tasks)
        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)
        # return JsonResponse("No status was specified!", safe=False)
        # 'safe=False' for objects serialization

    # elif request.method == 'DELETE':
    #     count = Tutorial.objects.all().delete()
    #     return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


# Create your views here.

def userList(request):

    if request.method == 'GET':
        userID = JSONParser().parse(request)
        tasks = Task.objects.all()

        tasks = tasks.filter(
            userID=userID['userID'])
        # print(tasks)
        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)


def comleteTask(request):

    if request.method == 'PUT':
        task_data = JSONParser().parse(request)
        tasks = Task.objects.all()

        try:
            task = tasks.get(
                Id=task_data['Id'])

            # task = tasks.get(
            #     Id=task_data['Id'])

            task_serializer = TaskSerializer(task, data=task_data)
            if task_serializer.is_valid():
                task_serializer.save()
                return JsonResponse("Updated Successfully", safe=False)
            return JsonResponse("Failed to Update")

        except Task.DoesNotExist:
            return JsonResponse({'message': 'The resord does not exist'}, status=status.HTTP_404_NOT_FOUND)


def userFilter(request):
    if request.method == 'GET':
        task_data = JSONParser().parse(request)
        tasks = Task.objects.all()

        tasks = tasks.filter(
            userID=task_data['userID'], status=task_data['status'])
        # print(tasks)
        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)
