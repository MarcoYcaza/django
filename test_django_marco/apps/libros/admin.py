from django.contrib import admin
from .models import Libro


class Libro_admin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Libro,Libro_admin)