from .models import  DataStructure, Method, Property
from rest_framework import serializers

class MethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Method
        fields = ['id', 'name', 'code_block', 'resource']

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'name', 'type', 'code_block', 'resource']



class DataStructureSerializer(serializers.ModelSerializer):
    methods = MethodSerializer(read_only=True, many=True)
    properties = PropertySerializer(read_only=True, many=True)
    #Meta provide info about model
    class Meta:
        model = DataStructure
        fields = ['id', 'name', 'description', 'element',
                  'properties', 'methods', 'user']


