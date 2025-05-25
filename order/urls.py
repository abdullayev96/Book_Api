from django.urls import path
from .views import OrderAPI



urlpatterns = [
          path('', OrderAPI.as_view())
]

