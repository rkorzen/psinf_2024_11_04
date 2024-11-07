from django.contrib import admin
from .models import Szkolenie
# Register your models here.


class SzkolenieAdmin(admin.ModelAdmin):
    list_display = ["title", "szkolenie_data"]

admin.site.register(Szkolenie, SzkolenieAdmin)