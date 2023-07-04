import datetime

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from tasks.models import *
from tasks.serializers import *


@api_view(['GET', 'POST'])
def tasks_list_api_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        data = TaskSerializer(tasks, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = request.data
        task = Task.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            completed=data.get('completed'),
            created=datetime.datetime.now()
        )
        return Response(data=TaskSerializer(task, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def task_api_view(request, **kwargs):
    task = Task.objects.get(id=kwargs['id'])
    if request.method == 'GET':
        data = TaskRetrieveSerilizer(task, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        data = request.data
        task.title = data.get('title')
        task.description = data.get('description')
        task.completed = data.get('completed')
        task.created = data.get('created')
        return Response(data=TaskRetrieveSerilizer(task, many=False).data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        data = request.data
        task.id = data.get('id', None)
        task.delete()
        return Response({'message': f'Task {task.title} is deleted'}, status=status.HTTP_204_NO_CONTENT)

