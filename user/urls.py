from django.urls import path
from .views import *


urlpatterns = [
    path("register/", registerUser, name="register"),
    path("sendSms/", sendSms, name="send-sms-code"),
    
    path("send_by_phone_number/", sendSmsByPhoneNumber, name="send_by_phone_number"),
    path("forget_password/", forgetPassword, name="forget_password"),
    
    path("verifycode/", verifyCode, name="verify-sms-code"),
    
    # path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/", loginUser, name="token_obtain_pair"),
    
    path("profile/", getUserProfile, name="user-profile"),
    path("profile/update/", updateUserProfile, name="user-profile-update"),
    path("", getUsers, name="users"),
    path("<str:pk>/", getUserById, name="user"),
    
    # only admin can use this one
    path("update/<str:pk>/", updateUser, name="user-update"),
    path("delete/<str:pk>/", deleteUser, name="user-delete"),
]
