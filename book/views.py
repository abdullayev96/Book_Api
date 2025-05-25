from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import *
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import status
from .serializers import *

from  django_filters.rest_framework import DjangoFilterBackend



class  BookRateAPI(CreateAPIView):
      queryset = BookRead.objects.all()
      serializer_class = ReadBookSerializer

      filterset_fields = ['name']

      # def create(self, request, *args, **kwargs):
      #     user = self.request.user

      # def post(self, request):
      #     try:
      #        data  = request.data
      #        serializer  = ReadBookSerializer(data=data)
      #        if serializer.is_valid(raise_exception=True):
      #           serializer.save()
      #           return Response({"status":status.HTTP_201_CREATED,
      #                         "data":serializer.data
      #                         })

      #     except Exception as e:
      #               print(e)

          #return Response({"status": status.HTTP_404_NOT_FOUND,
          #                         "data": serializer.errors})



#filter by category author performer


class BookAPI(ListAPIView):
      queryset = Book.objects.all()
      serializer_class = BookSerializer

      filter_backends = [DjangoFilterBackend]

      filterset_fields = ['category', 'author']


     # def get(self, request):
     #      try:
     #          user  = Book.objects.all()
     #          serializer = BookSerializer(user, many=True)
     #          return Response({'status':status.HTTP_200_OK, "data":serializer.data})
     #
     #      except Exception as e:
     #                print(e)



class BookDetailAPI(RetrieveAPIView):
      queryset = Book.objects.all()
      serializer_class = BookDetailSerializer



      # def get(self, request, pk=None):
      #     try:
      #        user = Book.objects.get(id=pk)
      #        serializer = BookDetailSerializer(user)
      #        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
      #
      #     except Exception as e:
      #               print(e)
      #
      #
      #     return Response({"status":status.HTTP_404_NOT_FOUND})



