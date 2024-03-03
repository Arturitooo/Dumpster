from rest_framework import serializers
from .models import Project

# Create your serializers here.


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "start_date", "end_date", "comments", "status"]
