from rest_framework.serializers import ModelSerializer
from .models import Feed

class FeedSerializers(ModelSerializer):
    class Meta:
        model = Feed
        fields = "__all__"

        depth = 1