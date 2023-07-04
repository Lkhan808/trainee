from rest_framework import serializers
from tasks.models import *


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

class TaskRetrieveSerilizer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'