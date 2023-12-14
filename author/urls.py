from django.urls import path
from .views import *


urlpatterns  = [
          path('', AuthorListAPI.as_view()),
          path('<int:author_id>/', AuthorRetrieveAPI.as_view()),

]