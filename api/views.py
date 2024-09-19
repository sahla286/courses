from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Courses,Student
from rest_framework import status
from rest_framework.response import Response
from .serializers import CourseModelSerializer,StudentModelSerializer
from rest_framework.decorators import action

# Create your views here.
class CourseViewset(ModelViewSet):
    serializer_class = CourseModelSerializer
    queryset = Courses.objects.all()
    
    @action(methods=['POST'], detail=True)
    def add_student(self, request, *args, **kw):
        id = kw.get('pk')
        course = self.queryset.get(id=id)
        ser = StudentModelSerializer(data=request.data)
        if ser.is_valid():
            name = ser.validated_data.get('name')
            age = ser.validated_data.get('age')
            email = ser.validated_data.get('email')
            qua = ser.validated_data.get('qua')
            Student.objects.create(name=name, age=age, email=email, qua=qua, course=course)
            return Response(data=ser.data, status=status.HTTP_200_OK)
        return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['GET'], detail=True)
    def get_student(self, request, *args, **kw):
        id = kw.get('pk')
        course = self.queryset.get(id=id)
        students=Student.objects.filter(course=course)
        ser = StudentModelSerializer(students,many=True)
        return Response(data=ser.data,status=status.HTTP_200_OK)
    
