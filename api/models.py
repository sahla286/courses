from django.db import models

# Create your models here.

class Courses(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    fee=models.PositiveIntegerField()
    seats=models.PositiveBigIntegerField()
    image=models.ImageField(upload_to='image',null=True)
    
    def __str__(self) :
        return self.title