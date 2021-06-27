

from rest_framework import serializers
from .models import College


class Collegeserializer(serializers.ModelSerializer):
     class Meta:
         model = College
         fields =  ['name','location','principal']


# name = serializers.CharField(max_length = 100)
    # location = serializers.CharField(max_length = 100)
    # principal = serializers.CharField(max_length = 100)
    #
    # def create(self, validate_data):
    #   return College.objects.create(validate_data)
    #
    # def update(self, instance, validate_data):
    #     instance.name = validate_data.get('name', instance.name)
    #     instance.location = validate_data.get('location', instance.location)
    #     instance.principal = validate_data.get('principal', instance.principal)
    #     instance.save()
    #     return instance
    #
