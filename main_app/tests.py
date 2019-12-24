from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class ModelTestCase(TestCase):
	def setUp(self):
		self.username = 'Chi'
		self.user = User(username=self.username)
	def test_model_can_create_a_user(self):
		old_count = User.objects.count()
		self.user.save()
		new_count = User.objects.count()
		self.assertNotEqual(old_count,new_count)