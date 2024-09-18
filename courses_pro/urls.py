from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter 

router=DefaultRouter()
router.register('api/courses',views.CourseViewset,basename='courses')

urlpatterns = [
    path('admin/', admin.site.urls),
]+ router.urls
