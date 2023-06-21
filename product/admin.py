from django.contrib import admin, messages
from product.models import ProductCategory, ProductVariation, ProductTag, Product, ProductImage




class ProductCategoryAdmin(admin.ModelAdmin):
    list_display=('name', 'status', 'show_on_homepage')
    list_filter=['status']
    search_fields=['name']
   
admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductVariationAdmin(admin.ModelAdmin):
    list_display=('name', 'status')
    search_fields=['name']
admin.site.register(ProductVariation, ProductVariationAdmin)

class ProductTagAdmin(admin.ModelAdmin):
    list_display=('name', 'status')
    search_fields=['name']

admin.site.register(ProductTag, ProductTagAdmin)


def active_status(modelAdmin, request, queryset):
 try:
          queryset.update(status=True)
          messages.success(request, 'Selacted records marked as active')
 except Exception as e:
     messages.error(request. str(e))
             

def inactive_status(modelAdmin, request, queryset):
  try:
          queryset.update(status=False)
          messages.success(request, 'Selacted records marked as active')
  except Exception as e:
          messages.error(request. str(e))
             

 #class ProductImageInline(admin.TabularInline):
# """Display child In table form"""
  #  model=ProductImage
class ProductImageInline(admin.StackedInline):
    """Display child form in row format""" 
    model=ProductImage

class ProductAdmin(admin.ModelAdmin):
   prepopulated_fields={'slug': ('name', )}
   list_display=('name', 'product_category', 'price', 'status')
   list_filter=['product_category']
   search_fields=['name']
   inlines=(ProductImageInline,)
   actions=(active_status, inactive_status)

admin.site.register(Product, ProductAdmin)

 