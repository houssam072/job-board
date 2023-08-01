from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Jop)
admin.site.register(Category)