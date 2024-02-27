from django.contrib import admin

from payment.models import Order, Item


class ItemTabularAdmin(admin.TabularInline):
    model = Item
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created')
    readonly_fields = ('created',)

    inlines = [ItemTabularAdmin]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'currency', 'order')
