from django.contrib import admin
from models import Decal


class DecalAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "buy_count")
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Decal, DecalAdmin)