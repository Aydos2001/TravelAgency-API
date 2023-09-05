from django.contrib import admin
from .models import *

admin.site.register(Destination)
admin.site.register(Booking)

@admin.register(Package)
class Packages(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}