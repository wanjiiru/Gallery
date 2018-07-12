from django.shortcuts import render
from .models import Image

# Create your views here.

def welcome(request):

    image = Image.save_image()
    print(image)
    return render(request,'welcome.html',{"image":image})