from rest_framework import serializers
from .models import Courses

class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields='__all__'