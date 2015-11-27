from django.contrib import admin
from models import Cart, Item


class CartAdmin(admin.ModelAdmin):
    list_display = ("creation_date",)


class ItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "unit_price", "quantity",)

#
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ("name", "phone", "price")


admin.site.register(Cart, CartAdmin)
admin.site.register(Item, ItemAdmin)
# admin.site.register(Order, OrderAdmin)