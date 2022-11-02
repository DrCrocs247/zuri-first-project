from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SlackDeveloper
from .serializers import SlackDeveloperSerializers

# Create your views here.

class developers_data(APIView):

    def get(self, request):
        developers = SlackDeveloper.objects.all()
        serializer = SlackDeveloperSerializers(developers, many=True)
        return Response(serializer.data)