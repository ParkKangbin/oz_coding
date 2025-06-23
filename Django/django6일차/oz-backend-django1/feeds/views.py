from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Feed
from .serializers import FeedSerializers
# Create your views here.
class Feeds(APIView):
    def get(self,request):
        feeds = Feed.objects.all() # 객체 
        # 객체 -> 시리얼 라이즈 해야지 제이슨 화해서 간다
        serializers = FeedSerializers(feeds, many=True)

        return Response(serializers.data)
    
    def post(self, request):
        serializer = FeedSerializers(data=request.data)
        if serializer.is_valid():
            feed = serializer.save(user=request.user)

            serializer = FeedSerializers(feed)
            

            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class FeedDetail(APIView):
    def get_object(self, feed_id):
        try:
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound
    
    def get(self, request, feed_id):
        feed = self.get_object(feed_id)

        serializer = FeedSerializers(feed)

        return Response(serializer.data)
