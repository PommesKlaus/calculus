from django.contrib import admin

# Register your models here.

from .models import Company, Year, Version

admin.site.register(Company)
admin.site.register(Year)
admin.site.register(Version)
