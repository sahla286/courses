from rest_framework import serializers
from .models import Courses,Student

class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields='__all__'

class StudentModelSerializer(serializers.ModelSerializer):
    # course=serializers.CharField(read_only=True) 
    course=CourseModelSerializer(read_only=True) 
    class Meta:
        model=Student
        fields='__all__'
