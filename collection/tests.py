from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        self.image = Image(name='test',pic='pic.jpg',description='tets4' ,image_location ='Location',image_category='Shoes')


    def test_instance(self):
        self.assertTrue(isinstance((self.image,Image)))