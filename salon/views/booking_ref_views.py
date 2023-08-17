from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from salon.models import BookingReference
from salon.serializers import BookingReferenceSerializer
from rest_framework.permissions import IsAdminUser


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def getBookingReference(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            court = get_object_or_404(BookingReference, id=pk)
            serializer = BookingReferenceSerializer(court)
            return Response(serializer.data, status=200)
        else:        
            data = BookingReference.objects.all()
            serializer = BookingReferenceSerializer(data, many=True)
            return Response(serializer.data, status=200)

    elif request.method == 'POST':
        serializer = BookingReferenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        court = get_object_or_404(BookingReference, pk=pk)
        serializer = BookingReferenceSerializer(court, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        court = get_object_or_404(BookingReference, pk=pk)
        court.delete()
        return Response({"message":"Delete Successful."}, status=status.HTTP_204_NO_CONTENT)
