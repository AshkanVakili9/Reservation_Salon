from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from salon.models import Reservation, AvailableTime
from salon.serializers import ReservationSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated


# // NextPay.IR Python Sample
# // docs : https://nextpay.org/nx/docs

# ////////////
# // step 1 //
# ////////////


# import requests

# url = "https://nextpay.org/nx/gateway/token"

# payload='api_key=b11ee9c3-d23d-414e-8b6e-f2370baac97b&amount=74250&order_id=85NX85s427&customer_phone=09121234567&custom_json_fields=%7B%20%22productName%22%3A%22Shoes752%22%20%2C%20%22id%22%3A52%20%7D&callback_uri=https%3A%2F%2FyourWebsite.com%2Fcallback'
# headers = {
#   'User-Agent': 'PostmanRuntime/7.26.8',
#   'Content-Type': 'application/x-www-form-urlencoded'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# # print(response.text)


# # ////////////
# # // step 5 //
# # ////////////


# import requests

# url = "https://nextpay.org/nx/gateway/verify"

# payload='api_key=b11ee9c3-d23d-414e-8b6e-f2370baac97b&amount=74250&trans_id=f7c07568-c6d1-4bee-87b1-4a9e5ed2e4c1'
# headers = {
#   'User-Agent': 'PostmanRuntime/7.26.8',
#   'Content-Type': 'application/x-www-form-urlencoded'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# # print(response.text)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def reservation_list(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reservation_detail_by_userID(request):
    user = request.user
    reservation = Reservation.objects.filter(user_id=user.id)
    serializer = ReservationSerializer(reservation, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reservation_detail(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    serializer = ReservationSerializer(reservation)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reservation_create(request):
    user = request.user
    data = request.data
    data['user'] = user.id
    serializer = ReservationSerializer(data=data)
    if serializer.is_valid():
        reservation = serializer.save()

        # Calculate total amount based on the selected available times
        available_times_ids = request.data.get('available_time', [])
        selected_times = AvailableTime.objects.filter(
            id__in=available_times_ids)
        total_amount = sum(time.court.price for time in selected_times)

        reservation.total_amount = total_amount
        reservation.save()

        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def reservation_update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    serializer = ReservationSerializer(
        reservation, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

        available_times_ids = request.data.get('available_time', [])
        selected_times = AvailableTime.objects.filter(
            id__in=available_times_ids)
        total_amount = sum(time.court.price for time in selected_times)

        reservation.total_amount = total_amount
        reservation.save()

        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    return Response({"detail": "Delete Successful."}, status=204)
