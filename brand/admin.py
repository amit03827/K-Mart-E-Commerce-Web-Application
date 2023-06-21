from django.contrib import admin
from brand .models import Brand

class BrandAdmin(admin.ModelAdmin):
    list_display=('name', 'status')

admin.site.register(Brand, BrandAdmin)

