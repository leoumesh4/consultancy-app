from django.db import models
from django.utils.timezone import now
from django.utils.safestring import mark_safe


class About(models.Model):
    class Meta:
        verbose_name_plural = "About"

    description = models.TextField(max_length=700, null=True)
    date_created = models.DateTimeField(default=now)
    about_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "About Info"

class Slider(models.Model):
    class Meta:
        verbose_name_plural = "Slider"

    main_heading = models.CharField(max_length=200, null=True)
    sub_heading = models.CharField(max_length=200, null=True)
    slider_caption = models.CharField(max_length=200, null=True, blank=True)
    slider_image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(default=now)


    def __str__(self):
        return self.slider_caption

class Gallery(models.Model):

    class Meta:
        verbose_name_plural = "Galleries"

    caption = models.CharField(max_length=200, blank=True, null=True)
    gallery_img = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(default=now)



    def __str__(self):
        return self.caption

class Team(models.Model):

    class Meta:
        verbose_name_plural = "Team"

    name = models.CharField(max_length=200, null=True)
    introduction = models.CharField(max_length=600, null=True)
    facebook_profile_link = models.CharField(max_length=300, null=True)
    instagram_profile_link = models.CharField(max_length=300, null=True)
    profile_image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class Subservice(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class ContactInfo(models.Model):

    class Meta:
        verbose_name_plural = "Contact Info"

    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    concern = models.TextField(max_length=500, null=True)

    def __str__(self):
        return (self.name+"'" + "s" + " " + "Query")



