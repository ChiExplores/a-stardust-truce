from django.test import Client
from django.test import TestCase


class Setup_Class(TestCase):
  def setUp(self):
      self.user = User.objects.create(email="user@structures.com", 
      password="user", 
      first_name="user")
      
  def test_secure_page(self):
    User = get_user_model()
    self.client.login(username='temporary', password='temporary')
    response = self.client.get('/structures/', follow=True)
    user = User.objects.get(username='temporary')
    self.assertEqual(response.context['email'], 'temporary@gmail.com')
  
  def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_autheticated)




