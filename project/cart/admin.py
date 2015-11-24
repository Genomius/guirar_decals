from django.contrib import admin
from models import Cart, DecalInCart, Order


class CartAdmin(admin.ModelAdmin):
    list_display = ("creation_date",)


class DecalInCartAdmin(admin.ModelAdmin):
    list_display = ("decal", "quantity",)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "price")


admin.site.register(Cart, CartAdmin)
admin.site.register(DecalInCart, DecalInCartAdmin)
admin.site.register(Order, OrderAdmin)