from .models import *
from rest_framework import serializers

class ResourceBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'name', 'description', 'img_url']

class CodeBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeBlock
        fields = ['id', 'name', 'python', 'javascript']


class MethodSerializer(serializers.ModelSerializer):
    code_block = CodeBlockSerializer(read_only=True)
    resource = ResourceBlockSerializer(read_only=True)
    class Meta:
        model = Method
        fields = ['id', 'name', 'code_block', 'resource']

class PropertySerializer(serializers.ModelSerializer):
    code_block = CodeBlockSerializer(read_only=True)
    resource = ResourceBlockSerializer(read_only=True)
    class Meta:
        model = Property
        fields = ['id', 'name', 'type', 'code_block', 'resource']

class ElementSerializer(serializers.ModelSerializer):
    code_block = CodeBlockSerializer(read_only=True)
    class Meta:
        model = Element
        fields = ['name', 'type', 'code_block', 'resource']

class DataStructureSerializer(serializers.ModelSerializer):
    methods = MethodSerializer(read_only=True, many=True)
    properties = PropertySerializer(read_only=True, many=True)
    element = ElementSerializer(read_only=True)
    #Meta provide info about model
    class Meta:
        model = DataStructure
        fields = ['id', 'name', 'description', 'element',
                  'properties', 'methods', 'user']


