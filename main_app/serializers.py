from django.contrib.auth.models import User
from rest_framework import serializers
# from .models import User


class DataStructureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'description', 'element',
                  'properties', 'methods', 'user']
