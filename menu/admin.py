from django.contrib import admin
from menu.models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ["name","ingrediants","process"]
# Register your models here.
admin.site.register(Menu)