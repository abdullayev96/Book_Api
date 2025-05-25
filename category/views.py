from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import Category
from rest_framework.generics import ListAPIView
from .serializers import CategorySerializer
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend



class CategoryAPI(ListAPIView):
      queryset = Category.objects.all()
      serializer_class = CategorySerializer

      filter_backends = [DjangoFilterBackend]
      filterset_fields = ['name']


      # def get(self, request):
      #     try:
      #        user  = Category.objects.all()
      #        serializer   = CategorySerializer(user, many=True)
      #        return Response({"status":status.HTTP_200_OK, "data":serializer.data})
      #
      #     except Exception as e:
      #               print(e)


