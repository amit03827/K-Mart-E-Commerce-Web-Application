from django.shortcuts import render
from product.models import ProductCategory, Product, ProductTag
from cms.models import WebsiteSetting, Slider, Blog, FAQs
from django.views import View


def home_page(request):
    """Home page of k mart of websit"""
    
    sliders = Slider.objects.filter(status=True)
    product_categorie=ProductCategory.objects.filter(status=True, show_on_homepage=True)[0:3]
    fashion_products_one=Product.objects.filter(status=True)[0:2]
    fashion_products_two=Product.objects.filter(status=True)[2:4]
    product_tags= ProductTag.objects.filter(status=True)[0:2]

    context={ 
        'sliders' : sliders,
        'product_categorie' : product_categorie,
        'fashion_products_one' : fashion_products_one,
        'fashion_products_two' : fashion_products_two,
        'product_tags' : product_tags
    }
    return render(request, 'home.html', context)
# This used for product id
#def product_listing(request, category_id):
#    navigation_categoris=ProductCategory.objects.filter(status=True)
#    website_seting=WebsiteSetting.objects.all().last()
    #products=Product.objects.filter(status=True, product_category=category_id)
#    products=Product.objects.filter(status=True, product_category_id=category_id)
#   print(products)

# Its Used for Slug
def product_listing(request, product_category_slug):
    #products=Product.objects.filter(status=True, product_category=category_id)
    products=Product.objects.filter(status=True, product_category__slug=product_category_slug)
    print(products)
    context={
         'products' : products
          
    }
    return render(request, 'product/product_listing.html', context)


class ProductDetails(View):

    def get(self, request, product_slug):
         #product_slug='denim'
         try:
            products = Product.objects.get(slug=product_slug)
            similar_products=Product.objects.filter(status=True, product_category=products.product_category).exclude(id=products.id)
            context={
              'products' : products,
              'similar_products' : similar_products,

               }
            return render(request, 'product/product_details.html', context)
         except Product.DoesNotExist:
             pass
