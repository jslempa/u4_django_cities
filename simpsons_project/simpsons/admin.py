from django.contrib import admin
from .models import City, Attraction, Review

# Register your models here.

admin.site.register(City)
admin.site.register(Attraction)
admin.site.register(Review)