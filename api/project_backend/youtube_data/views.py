
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from googleapiclient.discovery import build
from .models import Video, Channel
from .serializer import VideoSerializer, ChannelSerializer

def get_youtube_service():
    try:
        return build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
    except Exception as e:
        raise Exception(f"Error creating YouTube service: {str(e)}")

@api_view(['POST'])
def get_channel_info(channel_handle):
    try:
        service = get_youtube_service()
        params = {
            'part': 'contentDetails,id,snippet',
            'forHandle': channel_handle,  
        }
        request = service.channels().list(**params)
        response = request.execute()
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)})

@api_view(['POST'])
def get_video_info(video_url):
    try:
        service = get_youtube_service()
        params = {
            'part': 'snippet,statistics',
            'id': video_url.split('v=')[-1]  # Extract video ID from URL
        }
        request = service.videos().list(**params)
        response = request.execute()
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)})

