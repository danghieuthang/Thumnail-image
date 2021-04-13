
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from simple_image.views import image_view, success
  
urlpatterns = [
    path('upload/', image_view, name = 'image_upload'),
    path('success/', success, name = 'success'),
    path('admin/', admin.site.urls)
]
