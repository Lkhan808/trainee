from rest_framework import serializers
from tasks.models import *


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskRetrieveSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'