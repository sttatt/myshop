from django.contrib import admin
from .models import Product, Country, Company
from order.models import Order, TempProduct
# Register your models here.

class OrderItems(admin.TabularInline):
    model = TempProduct
    raw_id_fields = ['product']
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItems]
admin.site.register(Product)
admin.site.register(Country)
admin.site.register(Company)
admin.site.register(Order, OrderAdmin)
