from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializers
class FeedUserSerializers(ModelSerializer):
    
        user = FeedUserSerializers()
        class Meta:
            model = Feed
            # filter = "__all__"
            depth = 1
            fields = ("username", "email", "is_superuser",)
        