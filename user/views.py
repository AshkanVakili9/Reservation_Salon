from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User, Sms
from .serializers import UserSerializer, UserSerializerWithToken, SmsSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.hashers import make_password
from rest_framework import status
import random
import requests
import json
from django.shortcuts import get_object_or_404
from persian_tools import phone_number
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


def sms_send(request, phone, template_id):
    try:
        unique_id = str(random.randint(10000, 99999))
        url = "https://api.sms.ir/v1/send/verify"
        headers = {
            "X-API-KEY": "xLaqtCB7xkF6N4HB3OBSHbfPxZlMd8VXbpSOAuv3vFU5EPaTZcPqVMLhZw0lIvEW",
            "ACCEPT": "application/json",
            "Content-Type": "application/json",
        }
        sms_data = {
            "mobile": phone,
            "templateId": template_id,
            "parameters": [{"name": "CODE", "value": unique_id}],
        }
        request_sms = requests.post(
            url=url, headers=headers, data=json.dumps(sms_data), params=request.POST
        )
        sms_data = {"phone": phone, "sms": unique_id}
        sms_data_ser = SmsSerializer(data=sms_data)
        if sms_data_ser.is_valid():
            sms_data_ser.save()
        return True
    except Exception:
        return False


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data


""" login endpoint """


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


""" alternated by chatgpt """


@api_view(["POST"])
def registerUser(request):
    full_name = request.data.get('full_name')
    phone = phone_number.normalize(request.data.get('phone'))
    password = request.data.get('password')
    confirm_password = request.data.get('confirm_password')

    if not (full_name and phone and password and confirm_password):
        return Response({"error": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)

    if password != confirm_password:
        return Response({"error": "Passwords do not match."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(phone=phone)
        return Response({"error": "User already exists with this phone number."}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        pass

    data = {
        'full_name': full_name,
        'phone': phone,
        'password': make_password(password),
    }

    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()
        # Replace sms_send with the appropriate SMS sending implementation
        sms_send(request, phone=phone, template_id=245789)
        # Use UserSerializer instead of UserSerializerWithToken if no token is needed
        serializer_with_token = UserSerializerWithToken(user, many=False)
        return Response(serializer_with_token.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     
@api_view(["POST"])
def sendSmsByPhoneNumber(request):
    user_phone = phone_number.normalize(request.data['phone'])
    sms_send(request, phone=user_phone, template_id=245789)
    if sms_send:
        return Response("Sms has been Sent", status=status.HTTP_201_CREATED)
    return Response("Sms has been NoT Sent", status=status.HTTP_201_CREATED)

        
        
@api_view(["POST"])
def forgetPassword(request):
    user_phone = phone_number.normalize(request.data['phone'])
    code = request.data['code']
    password = request.data['password']
    confirm_password = request.data['confirm_password']
    
    check_code = Sms.objects.filter(phone=user_phone).latest("sentDate")
    if check_code.sms == code:
        check_code.is_matched = True
        check_code.save()
        user = User.objects.filter(phone=user_phone).first()
        if password == confirm_password:
            user.password = make_password(password)
            user.save()
            return Response({"message": "Password has been changed"}, status=status.HTTP_200_OK)
        return Response("Password does not match.", status=status.HTTP_400_BAD_REQUEST)
    return Response("Code does not match.", status=status.HTTP_400_BAD_REQUEST)
        

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def sendSms(request):
    user = request.user
    sms_send(request, phone=user.phone, template_id=245789)
    if sms_send:
        return Response("Sms has been Sent", status=status.HTTP_200_OK)
    return Response("Sms has been NoT Sent", status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def verifyCode(request):
    user = request.user
    code = request.data["code"]
    if code == None:
        return Response("Invalid Code", status=status.HTTP_400_BAD_REQUEST)
    user_sms = Sms.objects.filter(phone=user.phone).latest("sentDate")
    if user_sms is not None:
        if user_sms.sms == code:
            user.is_verified = True
            user.save()
            user_sms.is_matched = True
            user_sms.save()
            data = UserSerializer(user, many=False)
            return Response(
                {"message": "sms is true", "payload": data.data},
                status=status.HTTP_200_OK,
            )
        return Response("sms is Not true", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("phone Number in Not true", status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)

    data = request.data

    user.full_name = data["full_name"]

    if data["password"] != "":
        user.password = make_password(data["password"])

    user.save()
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAdminUser])
def getUserById(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAdminUser])
def updateUser(request, pk):
    user = User.objects.get(id=pk)

    data = request.data

    user.full_name = data["full_name"]
    user.email = data["email"]
    user.phone = data["phone"]
    user.password = make_password(data["password"])

    if data["isAdmin"] != "":
        user.isAdmin = data["isAdmin"]

    user.save()

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteUser(request, pk):
    user_for_deletion = get_object_or_404(User, id=pk)
    user_for_deletion.delete()
    return Response("User deleted successfully", status=status.HTTP_200_OK)
 