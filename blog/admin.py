from django.contrib import admin
from .models import *
from django.utils.html import format_html


class SliderAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.slider_image.url))

    image_tag.short_description = 'Slider Image Preview'

    # list_display = ['image_tag']: Using this will cause image to be displayed in list first while opening slider.
    readonly_fields = ['image_tag']

class AboutAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.about_pic.url))

    image_tag.short_description = 'Image Preview'
    # list_display = ['image_tag']
    readonly_fields = ['image_tag']

class GalleryAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.gallery_img.url))

    image_tag.short_description = 'Gallery Image Preview'
    # list_display = ['image_tag']
    readonly_fields = ['image_tag']

class TeamAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.profile_image.url))

    image_tag.short_description = 'Image Preview'
    # list_display = ['image_tag']
    readonly_fields = ['image_tag']

admin.site.register(About, AboutAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Service)
admin.site.register(Subservice)
admin.site.register(ContactInfo)
