from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20) # 짧은 문장
    description = models.TextField() # 긴 텍스트 문장
    age = models.PositiveIntegerField(null=True) # 양의 정수형 숫자 
    gender = models.CharField(max_length=10)