from django.urls import path
from django.contrib import admin
from . import views

admin.site.site_header = "Ricks Dashboard"
admin.site.site_title = "Ricks Construction"
admin.site.index_title = "Welcome to Ricks Construction"

urlpatterns = [
    path('', views.home, name="home"),
    path('services/', views.services, name="service"),
    path('team/', views.team, name="team"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
    path('contact/', views.contact, name="contact"),
]