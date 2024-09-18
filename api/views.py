from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Courses
from .serializers import CourseModelSerializer

# Create your views here.

class CourseViewset(ModelViewSet):
    serializer_class=CourseModelSerializer
    queryset=Courses.objects.all()