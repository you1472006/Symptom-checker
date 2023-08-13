from django.contrib import admin
from .models import Symptom,Disease

# Register your models here.
admin.site.register(Symptom)
admin.site.register(Disease)