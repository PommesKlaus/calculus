from django.contrib import admin

# Register your models here.

from .models import BsLineItem, Difference

admin.site.register(BsLineItem)
admin.site.register(Difference)