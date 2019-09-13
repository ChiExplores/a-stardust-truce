from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Code_Block(models.Model):
    python = models.TextField()
    javascript = models.TextField()

class Resource(models.Model):
    description = models.TextField()
    img_url = models.CharField()

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
        MaxValueValidator(2), # can be increased later
        MinValueValidator(1),
        default=1
    )
    code_block = models.ForeignKey(Code_Block, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)