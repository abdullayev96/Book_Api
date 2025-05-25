from rest_framework import serializers
from .models import Order
from account.models import CustomUser



class CustomUserSerializer(serializers.ModelSerializer):
     class Meta:
          model = CustomUser
          fields = ['username', 'email']




class OrderSerializer(serializers.ModelSerializer):

     class Meta:
          model  = Order
          fields  = ['book_name', 'author_name', 'comment']

