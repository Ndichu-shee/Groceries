from django.contrib import admin
from .models import Owner,Order,Customer,Product,ShippingAddress
# Register your models here.

admin.site.register(Owner)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(ShippingAddress)
