from django.urls import path

from .register import ValidateOTP, ValidatePhoneSendOTP
from .views import LogoutView, MyObtainTokenPairView,RegisterView, GetToken, ForgetPassword
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/s/', GetToken.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('forget-password/',ForgetPassword.as_view(),name="forget_password"),
    path('verify/',ValidatePhoneSendOTP.as_view(),name = "verify-password"),
    path('verify-otp/', ValidateOTP.as_view(),name="validate-otp")
]