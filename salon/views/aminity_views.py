
from salon.models import *
from salon.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

# Create your views here.


""" Amenity"""
@api_view(["POST"])
@permission_classes([IsAdminUser])
def addAminity(request):
    data = request.data
    serializer = AmenitySerializer(data=data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)

@api_view(["GET"])
@permission_classes([IsAdminUser])
def getAllAminity(request):
    amenity = Amenity.objects.all()
    serializer = AmenitySerializer(amenity, many=True)
    return Response(serializer.data, status=200)

@api_view(["GET"])
@permission_classes([IsAdminUser])
def getAminity(request, pk):
    amenity = get_object_or_404(Amenity, id=pk)
    serializer = AmenitySerializer(amenity)
    return Response(serializer.data, status=200)
    
@api_view(["PUT"])
@permission_classes([IsAdminUser])
def updateAminity(request, pk):
    data = request.data
    amenity = get_object_or_404(Amenity, id=pk)
    serializer = AmenitySerializer(amenity, data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)

@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteAminity(request, pk):
    amenity = get_object_or_404(Amenity, id=pk)
    amenity.delete()
    return Response({"message": "Successful, amenity Deleted."}, status=200)
    
