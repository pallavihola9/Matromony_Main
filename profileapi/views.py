from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics


# class Profile_register(generics.ListCreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

# class Profile_registerView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

class Profile_register(APIView):
    def get(self, request, format=None):
        Family = Profile.objects.all()
        serializer = ProfileSerializer(Family, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Profile_registerUpdateDeleteView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Profile, pk=pk)

    def get(self, request, pk):
        search = self.get_object(pk)
        serializer = ProfileSerializer(search)
        return Response(serializer.data)

    def put(self, request, pk):
        search = self.get_object(pk)
        serializer = ProfileSerializer(search, data=request.data, partial=True)

        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        search = self.get_object(pk)
        search.delete()
        return Response({"message":"Delete Successfully!!!"},status=status.HTTP_204_NO_CONTENT)