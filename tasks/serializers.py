from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields=[
            'id',
            'title',
            'description',
            'created_at',
            'updated_at',
            'is_complete',
        ]