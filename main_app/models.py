from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.urls import reverse
from main_app.dependencies import checkMethod, checkProperty, all_properties, all_methods
import re

# checkComponent signature
# checkComponent(component, data_structure, on_success, on_failure)

class CodeBlock(models.Model):
    name = models.CharField(max_length=50)
    python = models.TextField(max_length=300)
    javascript = models.TextField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Code Block"

class Resource(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    img_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name

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
    code_block = models.ForeignKey(CodeBlock, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Property(models.Model):
    name = models.CharField(max_length=50)
    STRING = 'str'
    INTEGER = 'int'
    FLOAT = 'float'
    SCALAR = 'sca'
    TYPE_CHOICES = (
        (STRING, 'String'),
        (INTEGER, 'Integer'),
        (FLOAT, 'Float'),
        (SCALAR, 'Scalar')
    )
    type = models.CharField(
        max_length=5,
        choices=TYPE_CHOICES,
        default=INTEGER
    )
    code_block = models.ForeignKey(CodeBlock, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

class Method(models.Model):
    name = models.CharField(max_length=50)
    code_block = models.ForeignKey(CodeBlock, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class DataStructure(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255, blank=True)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    properties = models.ManyToManyField(Property, blank=True)
    methods = models.ManyToManyField(Method, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}\'s {self.name}'

    def __get_js__(self):
        class_name = re.sub('\W', '', self.name)
        properties = self.properties.all()
        methods = self.methods.all()
        js = self.element.code_block.javascript + f'''
const {class_name} = _ => {{
  let obj = {{}}'''
        for property in properties:
            js += '\n' + property.code_block.javascript
        for method in methods:
            js += '\n' + method.code_block.javascript
        js += '''
  return obj
}'''
        return js

    def __get_py__(self):
        class_name = re.sub('\W', '', self.name)
        properties = self.properties.all()
        methods = self.methods.all()
        py = self.element.code_block.python + f'''
class {class_name}:
    def __init(self):'''
        for property in properties:
            py += '\n\t' + property.code_block.python
        for method in methods:
            py += '\n\t' + method.code_block.python
        return py

    def __get_valid_properties__(self):
        element = self.element.name
        valid_properties = []
        for property in all_properties:
            if checkProperty(property, element):
                valid_properties.append(property)
        return Property.objects.filter(name__in=valid_properties)

    def __get_valid_methods__(self):
        element = self.element.name
        properties = self.properties.all()
        valid_methods = []
        for method in all_methods:
            for property in properties:
                if checkMethod(method, element, property.name):
                    valid_methods.append(method)
        return Method.objects.filter(name__in=valid_methods)

    class Meta:
        verbose_name = "Data Structure"

    def get_absolute_url(self):
        return reverse('info', kwargs={'data_structures_id': self.id})