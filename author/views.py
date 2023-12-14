from django.shortcuts import render
from rest_framework.views import APIView,Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Author
from rest_framework import status
from .serializers import AuthorSerializer, AuthorDetailSerializer
from book.serializers import BookSerializer
from  django_filters.rest_framework import DjangoFilterBackend




class AuthorListAPI(ListAPIView):
      queryset = Author.objects.all()
      serializer_class = AuthorSerializer

      filter_backends = [DjangoFilterBackend]
      filterset_fields = ['full_name']



class AuthorRetrieveAPI(APIView):

      def get(self, request, author_id):
          try:
                author = Author.objects.get(id=author_id)
                serializer  = AuthorDetailSerializer(author)
                return Response({"status":status.HTTP_200_OK, "data":serializer.data})

          except Exception as e:
                print(e)

          return Response({"status": status.HTTP_404_NOT_FOUND})


