from rest_framework import serializers
from .models import Project, ProjectManager

# Create your serializers here.


class ProjectManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectManager
        fields = [
            "name",
            "id",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "projectmanager",
            "start_date",
            "end_date",
            "comments",
            "status",
        ]
