from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework import status
from account.models import CustomUser


#
# class OrderApi1(CreateAPIView):
#       serializer_class = OrderSerializer
#
#       def post(self, request, *args, **kwargs):
#           serializer = self.get_serializer(data=request.data)
#           serializer.is_valid(raise_exception=True)
#           user = serializer.save(user=request.user.username, status=Order.NEW)
#           return Response({"user": CustomUserSerializer(user, context=self.get_serializer_context()).data,})
#



class OrderAPI(GenericAPIView):
      permission_classes = [IsAuthenticated]
      serializer_class = OrderSerializer

      def post(self, request):
          try:
             serializer = self.get_serializer(data=request.data)
             serializer.is_valid(raise_exception=True)
             serializer.save(user=request.user, status=Order.NEW)

             return Response({"data":status.HTTP_201_CREATED})

          except Exception as e:
                    print(e)

          return Response({"status": status.HTTP_400_BAD_REQUEST})


