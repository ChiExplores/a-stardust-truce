from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Code_Block(models.Model):
    python = models.TextField(max_length=300)
    javascript = models.TextField(max_length=300)

class Resource(models.Model):
    description = models.TextField(max_length=255)
    img_url = models.CharField(max_length=100)

class Element(models.Model):
    name = models.CharField(max_length=50)
    NODE = 'NO'
    BLOCK = 'BL'
    TYPE_CHOICES = (
        (NODE, 'Node'), # a data element that stores a referent to other elements
        (BLOCK, 'Block') # a data element that stroes subelements in sequence
    )
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=NODE
    )
    dimension = models.IntegerField(
        validators = [
            MaxValueValidator(2), # can be increased later
            MinValueValidator(1),
        ],
        default=1
    )
    code_block = models.ForeignKey(Code_Block, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

class Property(models.Model):
    name = models.CharField(max_length=50)
    STRING = 'str'
    INTEGER = 'int'
    FLOAT = 'float'
    TYPE_CHOICES = (
        (STRING, 'String'),
        (INTEGER, 'Integer'),
        (FLOAT, 'Float')
    )
    type = models.CharField(
        max_length=5,
        choices=TYPE_CHOICES,
        default=INTEGER
    )
    code_block = models.ForeignKey(Code_Block, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

class Method(models.Model):
    name = models.CharField(max_length=50)
    code_block = models.ForeignKey(Code_Block, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

class Data_Structure(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    # element = models.ForeignKey(Element, on_delete=models.CASCADE)
    properties = models.ManyToManyField(Property)
    methods = models.ManyToManyField(Method)