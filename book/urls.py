from django.urls import path
from .views import *



urlpatterns  = [

          path('rate/', BookRateAPI.as_view()),

          path('', BookAPI.as_view()),
          path('<int:pk>/', BookDetailAPI.as_view()),

]


