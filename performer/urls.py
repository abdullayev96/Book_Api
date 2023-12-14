from django.urls import path
from .views import *


urlpatterns  = [

          path('', PerformerListAPI.as_view()),


]