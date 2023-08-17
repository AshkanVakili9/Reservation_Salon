from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from salon.models import Court
from salon.models import AvailableTime
from salon.serializers import AvailableTimeSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAdminUser])
def available_time_list(request):
    available_times = AvailableTime.objects.all()
    serializer = AvailableTimeSerializer(available_times, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def available_time_list_by_courtID(request, court_id):
    available_times = AvailableTime.objects.filter(court_id=court_id).order_by('start_end_time')
    serializer = AvailableTimeSerializer(available_times, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def available_time_create(request):
    data=request.data
    serializer = AvailableTimeSerializer()
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def available_time_update(request, pk):
    available_time = AvailableTime.objects.get(pk=pk)
    serializer = AvailableTimeSerializer(instance=available_time, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def available_time_delete(request, pk):
    available_time = AvailableTime.objects.get(pk=pk)
    available_time.delete()
    return Response(status=204)
