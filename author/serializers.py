from rest_framework import serializers
from .models import Author
from book.serializers import BookSerializer




class AuthorSerializer(serializers.ModelSerializer):
          class Meta:
              model = Author
              fields  =  ['id','photo', 'full_name','book_number']



class AuthorDetailSerializer(serializers.ModelSerializer):
          books = BookSerializer(many=True, read_only=True)
          class Meta:
              model = Author
              fields  =  ['photo','full_name','book_number', 'bio', 'books']

