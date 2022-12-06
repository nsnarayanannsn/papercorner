from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('gallery',views.gallery,name="gallery"),
    path('blog',views.blog,name="blog"),
    path('contact',views.contact,name="contact")
]