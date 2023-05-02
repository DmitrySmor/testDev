from django.contrib import admin
from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'url', 'parent']
    list_filter = ['parent']
    search_fields = ['name', 'url']
