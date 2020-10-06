from django.contrib import admin
from app.models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass

# Register your models here.
