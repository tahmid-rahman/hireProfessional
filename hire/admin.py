from django.contrib import admin

# Register your models here.
from .models import HirePost ,Professional

admin.site.register(HirePost)
admin.site.register(Professional)