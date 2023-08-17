from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from salon.models import Court
from salon.serializers import CourtSerializer
from rest_framework.permissions import IsAdminUser


@api_view(['GET'])
def courtByShahr(request, shahrestan):
    courts = Court.objects.filter(salon__location__shahrestan_id=shahrestan)
    serializer = CourtSerializer(courts, many=True)
    return Response(serializer.data)
    
    
    

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def court(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            court = get_object_or_404(Court, pk=pk)
            serializer = CourtSerializer(court)
            return Response(serializer.data)
        else:
            courts = Court.objects.all()
            serializer = CourtSerializer(courts, many=True)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CourtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        court = get_object_or_404(Court, pk=pk)
        serializer = CourtSerializer(court, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        court = get_object_or_404(Court, pk=pk)
        court.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
