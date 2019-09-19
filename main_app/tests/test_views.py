from django.test import TestCase, Client
from django.http import HttpRequest
from django.urls import reverse
from main_app.models import DataStructure


class ViewTest(TestCase):

  def test_homepage(self):
    response = self.client.get('/structures/')
    self.assertEqual(response.status_code,200)


  def test_structures_create(self):
    response = self.client.get('/structures/create/')
    self.assertEqual(response.status_code, 200)

  def test_structures_index_1(self):
    response = self.client.get('/structures/?id=f1/', follow=True)
    self.assertEqual(response.status_code, 200)

  
  def test_structures_delete(self):
    response = self.client.get('/structures/?id=1/delete', folow=True)
    self.assertEqual(response.status_code, 200)

  def test_structures_update(self):
    response = self.client.get('/structures/?id=5/update')
    self.assertEqual(response.status_code, 200)

  # def test_login(self):
  #   response = self.client.get('/login/')
  #   self.assertEqual(response.status_code, 200)



class UserPost(TestCase):
  @classmethod
  def setUpClass(self):
    self.client = Client()

''' Adding Account into the application '''
def test_addAccount(self):
  response = self.client.post('/',{'username':'name','password':'pass', 'email':'mail@mail.com'})
  self.assertEqual(response.status_code, 302)

class DSTests(TestCase):
  def setUp(self):
      ds = DataStructure.objects.get(id=1)
      print(ds)

  def test_des_content(self):
      ds = DataStructure.objects.get(id=1)
      expected_object_name = f'{ds.name}'
      self.assertEquals(expected_object_name, 'More Arrays')

  # def test_ds_list_view(self):
  #     response = self.client.get(reverse('detail'))
  #     self.assertEqual(response.status_code, 200)
  #     self.assertContains(response, 'just a test')
  #     self.assertTemplateUsed(response, 'detail.html')












# 401 unauthorized. User accessing things they should/'t
#testing routes
#looking at put request, and validating fields that we dont want to allow.