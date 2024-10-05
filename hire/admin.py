from django.contrib import admin

# Register your models here.
from .models import BidForJob, HirePost ,Professional



admin.site.register(HirePost)
admin.site.register(Professional)
admin.site.register(BidForJob)