from django.shortcuts import render
from rest_framework.views import APIView,  Response
from rest_framework.generics import GenericAPIView
from .serializers import *
from .emails import *
from rest_framework import status
from .models import CustomUser
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate



from django.middleware import csrf
from rest_framework_simplejwt.tokens import RefreshToken



class RegisterAPI(APIView):
      def post(self, request):
          try:
             data = request.data
             serializer = RegisterSerializer(data=data)
             if serializer.is_valid():
                serializer.save()
                send_otp_email(serializer.data['email'])
                return Response(serializer.data, status=status.HTTP_201_CREATED)


             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


          except Exception as e:
                    print(e)




class VerifyAPI(APIView):
      def post(self, request):
          try:
              serializer  = VerifySerializer(data=request.data)
              if serializer.is_valid():
                   email  = serializer.data['email']
                   otp   = serializer.data['otp']

                   user = CustomUser.objects.filter(email=email)
                   if not user.exists():
                         return Response({"status": status.HTTP_400_BAD_REQUEST,
                                 "message": "Try again IT is wrong ",
                                 "data": "Invalid OTP or email"})

                   if not user[0].otp != otp:
                         return Response({"status": status.HTTP_400_BAD_REQUEST,
                           "message": "try again It is wrong ",
                           "data": "wrong  OTP "})

                   user  = user.first()
                   user.is_staff = True
                   user.save()

                   return Response({"status": status.HTTP_200_OK,
                                  "message": "Your account activate",
                                  "data": serializer.data})


              return Response({"status": status.HTTP_400_BAD_REQUEST,
                               "message": "Try again It is wrong ",
                               "data": serializer.errors})

          except Exception as e:
                    print(e)




def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {

        "code": status.HTTP_200_OK,
        "msg": "Ok",
        'access_token': str(refresh.access_token),
    }



class LoginAPI(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            data = request.data
            #serializer = LoginSerializer(data=data)
            serializer = self.get_serializer(data=data)

            if serializer.is_valid():
                email = serializer.validated_data["email"]
                password = serializer.validated_data["password"]

                user = authenticate(request, email=email, password=password)

                data = get_tokens_for_user(user)

                return Response(data, status=status.HTTP_200_OK)

            else:
                return Response({'detail': 'Invalid credentials', 'status': status.HTTP_401_UNAUTHORIZED},
                                status=status.HTTP_401_UNAUTHORIZED)


        except Exception as e:
            print(e)

        return Response({'status': status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)


#
#
# class LoginAPI(APIView):
#     def post(self,request):
#         try:
#            serializer = LoginSerializer(data = request.data)
#            if serializer.is_valid():
#               email = serializer.validated_data["email"]
#               password = serializer.validated_data["password"]
#
#               user = authenticate(request, email=email, password=password)
#
#               data = get_tokens_for_user(user)
#               return Response({'data': data})
#
#         except Exception as e:
#             print(e)
#
#
#         return Response({'status': status.HTTP_404_NOT_FOUND})
#
