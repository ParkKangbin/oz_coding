from rest_framework.serializers import ModelSerializer
from .models import User


class MyinfoUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
class FeedUserSerializers(ModelSerializer):
    class Meta:
        model = User
            # filter = "__all__"
        fields = ("username", "email", "is_superuser",)
        