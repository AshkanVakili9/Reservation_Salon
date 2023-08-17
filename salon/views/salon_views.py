from salon.models import *
from salon.serializers import *
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@api_view(["POST"])
@permission_classes([IsAdminUser])
def addSalon(request):
    user = request.user
    data = request.data
    data['user'] = user.id
    serializer = SalonSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Successful, Salon Created."}, status=201)
    return Response({"message": "Failed", "payload": serializer.errors}, status=400)


@api_view(["GET"])
def getAllSalon(request):
    query = request.query_params.get("keyword")
    if query == None:
        query = ""

    salons = Salon.objects.filter(name__icontains=query)

    page = request.query_params.get("page")
    paginator = Paginator(salons, 10)

    try:
        salons = paginator.page(page)
    except PageNotAnInteger:
        salons = paginator.page(1)
    except EmptyPage:
        salons = paginator.page(paginator.num_pages)

    if page == None:
        page = 1

    page = int(page)

    serializer = SalonSerializerAll(salons, many=True)
    return Response(
        {"salons": serializer.data, "page": page, "pages": paginator.num_pages}
    )


@api_view(["GET"])
def getSalon(request, pk):
    salon_data = get_object_or_404(Salon, id=pk)
    serializer = SalonSerializer(salon_data)
    return Response({"message": "Here is the salon", "payload": serializer.data}, status=200)


@api_view(["PUT"])
@permission_classes([IsAdminUser])
def updateSalon(request, pk):
    data = request.data
    salon_data = get_object_or_404(Salon, id=pk)
    serializer = SalonSerializer(salon_data, data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Salon Updated Successfully", "payload": serializer.data}, status=206)
    return Response({'message': 'Failed', 'payload': serializer.errors}, status=400)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteSalon(request, pk):
    amenity = get_object_or_404(Salon, id=pk)
    amenity.delete()
    return Response({"message": "Successful, amenity Deleted."}, status=200)


""" Salon Images"""
@api_view(["POST"])
@permission_classes([IsAdminUser])
def addSalonImage(request):
    data = request.data
    serializer = SalonImageSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Successful", "payload": serializer.data}, status=200)
    return Response({"message": "Fails", "payload": serializer.errors}, status=400)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteSalonImage(request, pk):
    data = get_object_or_404(SalonImage, id=pk)
    data.delete()
    return Response({"message": "Successful, Image Deleted."}, status=200)


@api_view(['GET'])
# @permission_classes([AllowAny])
def getTopRatedSalons(request):
    # Get the top 5 salons by rating
    top_rated_salons = Salon.objects.filter().order_by('-rating')[:5]
    
    if top_rated_salons.exists():
        serializer = SalonSerializerAll(top_rated_salons, many=True)
        return Response({"message": "Successfully retrieved top rated salons", "payload": serializer.data}, status=200)
    else:
        return Response({"message": "No salons found"}, status=404)
