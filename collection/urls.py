from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^search/',views.search_image,name='search_image'),
    url(r'^category/',views.category),
    url(r'^location/(?P<loc>\w+)/', views.get_image_by_location, name='location')


   

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
