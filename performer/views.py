from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Performer
from .serializers import PerformerSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated



class PerformerListAPI(ListAPIView):
      queryset = Performer.objects.all()
      serializer_class = PerformerSerializer
      permission_classes = [IsAuthenticated]

      filter_backends = [DjangoFilterBackend]
      filterset_fields = ['full_name']


