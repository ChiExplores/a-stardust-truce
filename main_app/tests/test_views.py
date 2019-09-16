from django.test import TestCase, Client
from django.http import HttpRequest
# from django.test import SimpleTestCase
# from django.urls import reverse



class ViewTest(TestCase):

  def test_homepage(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code,200)

  def test_aboutpage(self):
    response = self.client.get('/about')
    self.assertEqual(response.status_code, 200)

  def test_structures(self):
    response = self.client.get('/structures')
    self.assertEqual(response.status_code, 200)

  def test_structures_create(self):
    response = self.client.get('/structures/create')
    self.assertEqual(response.status_code, 200)


# 401 unauthorized. User accessing things they should/'t
#testing routes
#looking at put request, and validating fields that we dont want to allow.