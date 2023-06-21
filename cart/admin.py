from django.contrib import admin
from cart .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display=('user','product', 'variation')

admin.site.register(Cart, CartAdmin)
