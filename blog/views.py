from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.contrib import messages

def home(request):
    about_us = About.objects.all()
    image_slider = Slider.objects.all()
    context = {'about_us': about_us, 'image_slider': image_slider}
    return render(request, 'blog/home.html', context)

def services(request):
    service_info = Service.objects.all()
    context = {'service_info': service_info}
    return render(request, 'blog/services.html', context)

def team(request):
    team_info = Team.objects.all()
    context = {'team_info': team_info}
    return render(request, 'blog/team.html', context)

def gallery(request):
    gallery_images = Gallery.objects.all()
    context = {'gallery_images': gallery_images}
    return render(request, 'blog/gallery.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        concern = request.POST.get("concern")

        contact_info = ContactInfo(name=name, email=email, phone=phone, concern=concern)
        contact_info.save()
        messages.success(request, "Your query has been received successfully.")
    return render(request, 'blog/contact.html')



