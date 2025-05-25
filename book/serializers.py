from rest_framework import serializers
from account.models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import *



class BookCategorySerializer(serializers.ModelSerializer):
      class Meta:
          model = Category
          fields = ['id', 'name']


class BookAuthorSerializer(serializers.ModelSerializer):
      class Meta:
          model = Author
          fields = ['id', 'full_name']



class BookFileSerializer(serializers.ModelSerializer):
      class Meta:
          model = FileBook
          fields = ['file']



class BookSerializer(serializers.ModelSerializer):
          category = BookCategorySerializer()
          author  = BookAuthorSerializer()

          # category  = serializers.SerializerMethodField()
          # author = serializers.SerializerMethodField()


          # def get_category(self, obj):
          #     if obj.category:
          #           return obj.category.name
          #     return None
          #
          #
          # def get_author(self, obj):
          #     if obj.author:
          #           return obj.author.full_name
          #     return None


          class Meta:
               model = Book
               fields = ['id','image', 'name', 'author', 'category']


class BookDetailSerializer(serializers.ModelSerializer):
      performer  = serializers.SerializerMethodField()
      category = serializers.SerializerMethodField()
      author = serializers.SerializerMethodField()
      files = BookFileSerializer(many=True, read_only=True)


      def get_performer(self, obj):
          if obj.performer:
               return obj.performer.full_name
          return None


      def get_category(self, obj):
          if obj.category:
              return obj.category.name
          return None


      def get_author(self, obj):
          if obj.author:
               return obj.author.full_name
          return None

      class Meta:
          model = Book
          fields = ['image', 'name', 'author', 'created_at','performer','category', 'description', 'files']



class ReadBookSerializer(serializers.ModelSerializer):
      book = serializers.SerializerMethodField()


      def get_book(self, obj):
          if obj.book:
             return obj.book.name
          return None


      class Meta:
          model = BookRead
          fields = ['book', 'score']



