from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from salon.models import Reserve, AvailableTime, OrderTime
from salon.serializers import ReserveSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated



@api_view(['GET'])
@permission_classes([IsAdminUser])
def reservation_list(request):
    reservations = Reserve.objects.all()
    serializer = ReserveSerializer(reservations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reservation_detail_by_userID(request):
    user = request.user
    reservation = Reserve.objects.filter(user_id=user.id)
    serializer = ReserveSerializer(reservation, many=True)
    return Response(serializer.data, status=200)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reservation_detail(request, pk):
    reservation = Reserve.objects.get(pk=pk)
    serializer = ReserveSerializer(reservation)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reservation_create(request):
    user = request.user
    data = request.data
    orderTimes = data.get('orderTimes', [])

    if not orderTimes:
        return Response({"detail": "No order times provided"}, status=400)

    # Calculate total amount based on selected order times
    total_amount = sum(order["price"] * order["qty"] for order in orderTimes)

    # Create a reservation
    reserve_data = {
        "user": user.id,
        "payment_method": data.get("payment_method", ""),
        "total_amount": total_amount,
        "paid_at": data.get("paid_at", None),
        "is_paid": data.get("is_paid", False),
    }
    reserve_serializer = ReserveSerializer(data=reserve_data)

    if reserve_serializer.is_valid():
        reservation = reserve_serializer.save()

        # Create order times and set the reservation
        for order in orderTimes:
            available_time = AvailableTime.objects.get(id=order["time"])
            OrderTime.objects.create(
                available_time=available_time,
                reserve=reservation,
                qty=order["qty"],
                price=order["price"],
            )

        return Response(reserve_serializer.data, status=201)

    return Response(reserve_serializer.errors, status=400)



# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def reservation_create(request):
#     user = request.user
#     data = request.data
#     orderTimes = data['orderTimes']
#     if orderTimes and len(orderTimes) == 0:
#         return Response({"detail": "No order times"}, status=400)
#     else:
#         # Create order
#         reserve = Reserve.objects.create(
#             user=user,
#             payment_method=data['payment_method'],
#             total_amount=data['total_amount'],
#             paid_at=data['paid_at'],
#             is_paid=data['is_paid'],
#         )
#         # Create order times and set order to orderTime relationship
#         for i in orderTimes:
#             available_time = AvailableTime.objects.get(id=i["time"])
#             item = OrderTime.objects.create(
#                 available_time=available_time,
#                 reserve=reserve,
#                 qty=i["qty"],
#                 price=i["price"],
#             )
#         serializer = ReserveSerializer(reserve, many=False)
#         return Response(serializer.data, status=201)
        
        
#         # serializer = ReserveSerializer(data=data)
#         # if serializer.is_valid():
#         #     reservation = serializer.save()

#         #     # Calculate total amount based on the selected available times
#         #     available_times_ids = request.data.get('available_time', [])
#         #     selected_times = AvailableTime.objects.filter(
#         #         id__in=available_times_ids)
#         #     total_amount = sum(time.court.price for time in selected_times)

#         #     reservation.total_amount = total_amount
#         #     reservation.save()

#         #     return Response(serializer.data, status=201)
#         # return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def reservation_update(request, pk):
    reservation = get_object_or_404(Reserve, pk=pk)
    serializer = ReserveSerializer(
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
    reservation = get_object_or_404(Reserve, pk=pk)
    reservation.delete()
    return Response({"detail": "Delete Successful."}, status=204)



# import logging
# from django.urls import reverse
# from django.shortcuts import render
# from azbankgateways import bankfactories, models as bank_models, default_settings as settings
# from azbankgateways.exceptions import AZBankGatewaysException


# def go_to_gateway_view(request):
#     # خواندن مبلغ از هر جایی که مد نظر است
#     amount = 1000
#     # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
#     user_mobile_number = '+989112221234'  # اختیاری

#     factory = bankfactories.BankFactory()
#     try:
#         bank = factory.auto_create() # or factory.create(bank_models.BankType.BMI) or set identifier
#         bank.set_request(request)
#         bank.set_amount(amount)
#         # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
#         bank.set_client_callback_url(reverse('callback-gateway'))
#         bank.set_mobile_number(user_mobile_number)  # اختیاری
    
#         # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
#         # پرداخت برقرار کنید. 
#         bank_record = bank.ready()
        
#         # هدایت کاربر به درگاه بانک
#         context = bank.get_gateway()
#         return render(request, 'redirect_to_bank.html', context=context)
#     except AZBankGatewaysException as e:
#         logging.critical(e)
#         return render(request, 'redirect_to_bank.html')
