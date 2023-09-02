from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from salon.models import Location
from salon.serializers import LocationSerializer
from rest_framework.permissions import IsAdminUser


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_all_locations(request, pk=None):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_location(request, pk):
    location = get_object_or_404(Location, id=pk)
    serializer = LocationSerializer(location, many=False)
    return Response(serializer.data)


# @api_view(['POST'])
# @permission_classes([IsAdminUser])
# def create_location(request):
#     data = request.data
#     check_salon_location = Location.objects.filter(salon_id=data['salon'])
#     if check_salon_location:
#         return Response({"message": "This salon has a address already."}, status=400)
#     if check_salon_location == False:
#         return Response({"message": "Salon doesn't exist."}, status=400)
#     else:    
#         serializer = LocationSerializer(data=data, many=False)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


# @api_view(['PUT'])
# @permission_classes([IsAdminUser])
# def update_location(request, pk):
#     location = get_object_or_404(Location, pk=pk)
#     serializer = LocationSerializer(location, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=400)


# @api_view(['DELETE'])
# @permission_classes([IsAdminUser])
# def delete_location(request, pk):
#     location = get_object_or_404(Location, pk=pk)
#     location.delete()
#     return Response({"message": "Delete was Successful."}, status=204)
