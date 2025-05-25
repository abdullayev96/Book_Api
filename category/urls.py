from django.urls import path
from .views import CategoryAPI

#todo: change tot category

# select list category/author / performer

urlpatterns  = [
          path('', CategoryAPI.as_view()),

]