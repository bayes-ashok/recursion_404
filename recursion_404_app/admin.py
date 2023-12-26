from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Location)
admin.site.register(models.Signup)
admin.site.register(models.Reports)
admin.site.register(models.Event)