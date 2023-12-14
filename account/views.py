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

                # return Response({"status": status.HTTP_201_CREATED,
                #                  "message": "successfully registration check email",
                #                  "data": serializer.data})

             # return Response({"status": status.HTTP_400_BAD_REQUEST,
             #                  "message": "try again It is wrong ",
             #                  "data": serializer.errors})


             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


          except Exception as e:
                    print(e)



# class RegisterAPI(APIView):
#       def post(self,request):
#             serializer = RegisterSerializer(data = request.data)
#             if serializer.is_valid():
#                     serializer.save()
#                     send_otp_email(serializer.data['email'])
#                     res = { 'status' : status.HTTP_201_CREATED }
#                     return Response(res, status = status.HTTP_201_CREATED)
#             res = { 'status' : status.HTTP_400_BAD_REQUEST, 'data' : serializer.errors }
#             return Response(res, status = status.HTTP_400_BAD_REQUEST)


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
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
    }



class LoginAPI(APIView):
    def post(self,request):
        try:
           serializer = LoginSerializer(data = request.data)
           if serializer.is_valid():
              email = serializer.validated_data["email"]
              password = serializer.validated_data["password"]

              user = authenticate(request, email=email, password=password)

              data = get_tokens_for_user(user)
              return Response({'data': data})

        except Exception as e:
            print(e)


        return Response({'status': status.HTTP_404_NOT_FOUND})


# class LoginAPI(APIView):
#     def post(self, request):
#         try:
#            email = request.data.get('email')
#            password = request.data.get('password')
#
#            user = authenticate(email=email, password=password)
#
#            data = get_tokens_for_user(user)
#            return Response({'data': data})
#
#         except Exception as e:
#             print(e)
#
#
#         return  Response({'status':status.HTTP_404_NOT_FOUND})
#




# class LoginAPI(GenericAPIView):
#
#       serializer_class = LoginSerializer
#       def post(self, request):
#           try:
#               username = request.data.get('username', None)
#               password = request.data.get('password', None)
#
#               user = authenticate(username=username, password=password)
#               if user is not None:
#                   return Response(status=status.HTTP_200_OK,  data={'email':user.email})
#               else:
#                   return Response(status=status.HTTP_400_BAD_REQUEST, data={'message':"user doesn't exist"})
#
#
#
#           except Exception as e:
#                     print(e)
#



# class LoginAPI(GenericAPIView):
#     serializer_class = LoginSerializer
#
#
#     def post(self, request, format=None):
#         data = request.data
#         username = data.get('username', None)
#         password = data.get('password', None)
#
#
#         user = authenticate(request, username=username, password=password)
#         print(user)
#         if user is not None:
#             if user.is_staff:
#                 serializer  = self.serializer_class(data=data)
#                 serializer.is_valid(raise_exception=True)
#                 serializer.save()
#                 return Response({"Success": "Login successfully"})
#
#             else:
#                 return Response({"No active": "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response({"Invalid": "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)
#

