from cms.models import WebsiteSetting
from cart.models import Cart

def website_seting(request):
    website_seting=WebsiteSetting.objects.all().last()
    return { 'global_website_seting' : website_seting,}

def cart_count(request):
    """Display cart count on website header """
    quantity=0
    if request.user.is_authenticated:
      """Note: optimize this queary"""
      carts=Cart.objects.filter(user=request.user)
      for cart in carts:
           quantity = quantity + cart.quantity
    return {'global_cart_quantity' : quantity }    
