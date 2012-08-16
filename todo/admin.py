from django.contrib import admin
from models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "priority", "difficulty", "created", "done"]
    search_fields = ["name"]

admin.site.register(Item, ItemAdmin)
