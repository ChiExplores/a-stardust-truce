from django.test import TestCase, Client
from django.http import HttpRequest
from django.contrib.auth.models import User
from main_app.models import *

class Setup_Class(TestCase):
  def setUp(self):
      self.user = User.objects.create(email="user@structures.com", 
      password="user", 
      first_name="user")
      
  def test_secure_page(self):
    # User = get_user_model()
    self.client.login(username='temporary', password='temporary')
    response = self.client.get('/structures/', follow=True)
    user = User.objects.get(username='temporary')
    self.assertEqual(response.context['email'], 'temporary@gmail.com')
  
  def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_autheticated)


class UserPost(TestCase):
  @classmethod
  def setUpClass(self):
    self.client = Client()

''' Adding Account into the application '''
def test_addAccount(self):
  response = self.client.post('/',{'username':'name','password':'pass', 'email':'mail@mail.com'})
  self.assertEqual(response.status_code, 302)



