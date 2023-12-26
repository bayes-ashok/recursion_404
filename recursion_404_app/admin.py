from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Location)
admin.site.register(models.User)
admin.site.register(models.Reports)
admin.site.register(models.Event)
admin.site.register(models.poll)