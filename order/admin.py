from django.contrib import admin
from order .models import Order, OrderDetails



class OrderDetailesInline(admin.StackedInline):
    model=OrderDetails


class OrderAdmin(admin.ModelAdmin):
    list_display=('user', 'date_time', 'address', 'mobile', 'payment', 'status')
    inlines=(OrderDetailesInline, )
admin.site.register(Order, OrderAdmin)

class OrderDetailesAdmin(admin.ModelAdmin):
  list_display=('order', 'product', 'quantity', 'price')
admin.site.register(OrderDetails, OrderDetailesAdmin)



