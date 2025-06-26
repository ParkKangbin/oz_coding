from rest_framework.serializers import ModelSerializer
from .models import Review
from users.serializers import FeedUserSerializers

class ReviewSerializer(ModelSerializer):
    user = FeedUserSerializers()
    class Meta:
        model = Review
        fields = "__all__"

