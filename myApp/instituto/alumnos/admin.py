from django.contrib import admin # type: ignore
from .models import Genero, Usuario

# Register your models here.
admin.site.register(Genero)
admin.site.register(Usuario)