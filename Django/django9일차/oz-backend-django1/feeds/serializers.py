from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializers
from reviews.serializers import ReviewSerializer

class FeedSerializers(ModelSerializer):
    user = FeedUserSerializers(read_only=True)
    review_set = ReviewSerializer(many=True,read_only=True)


    class Meta:
        model = Feed
        fields = "__all__"

        depth = 1