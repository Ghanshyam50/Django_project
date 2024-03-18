# serializers.py

from rest_framework import serializers
from .models import ClientModel, ProjectModel

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = ['id', 'client_name', 'created_at', 'created_by']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']
