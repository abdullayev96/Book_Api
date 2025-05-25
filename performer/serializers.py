from rest_framework import serializers
from .models import Performer


class PerformerSerializer(serializers.ModelSerializer):

     class Meta:
          model = Performer
          fields = ['id','photo','full_name']




#
# class PerformerDetailSerializer(serializers.ModelSerializer):
#       author = serializers.SerializerMethodField()
#       category = serializers.SerializerMethodField()
#       audio = serializers.SerializerMethodField()
#
#
#       def get_author(self, obj):
#           if obj.author:
#               return obj.author.full_name
#           return None
#
#       def get_audio(self, obj):
#           file = obj.audio.all().values_list('file', flat=True)
#           return file
#
#       def get_category(self, obj):
#           if obj.category:
#                return obj.category.name
#           return None
#
#
#       class Meta:
#           model = Performer
#           fields = ['author', 'full_name','category', 'audio']
#
