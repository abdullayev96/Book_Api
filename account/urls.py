from django.urls import path
from .views import RegisterAPI, VerifyAPI,LoginAPI
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView



urlpatterns = [
          path('register/', RegisterAPI.as_view()),
          path('verify/', VerifyAPI.as_view()),
          path('login/', LoginAPI.as_view()),
          path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
          path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]