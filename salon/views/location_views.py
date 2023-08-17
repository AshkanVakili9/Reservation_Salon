from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from salon.models import Location
from salon.serializers import LocationSerializer
from rest_framework.permissions import IsAdminUser



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def location(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            location = get_object_or_404(Location, pk=pk)
            serializer = LocationSerializer(location)
            return Response(serializer.data)
        else:
            locations = Location.objects.all()
            serializer = LocationSerializer(locations, many=True)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        check_salon_location = Location.objects.filter(salon_id=data['salon'])
        if check_salon_location is None:
            serializer = LocationSerializer(data=data, many=False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response({"message":"Location already exists for this Salon"}, status=400)
    
    elif request.method == 'PUT':
        location = get_object_or_404(Location, pk=pk)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        location = get_object_or_404(Location, pk=pk)
        location.delete()
        return Response({"message":"Delete was Successful."}, status=204)
