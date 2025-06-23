from django.db import models

# Create your models here.
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # 데이터 베이스의 테이블 위에 컬럼이 추가되지않는다(위에 컬럼들)
