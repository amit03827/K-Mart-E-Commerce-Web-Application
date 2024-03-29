from django.shortcuts import render, redirect
from cart.models import Cart
from django.contrib.auth.decorators import login_required
from product.models import Product





@login_required
def add_to_cart_view(request):
    """ Handle add to cart form """
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        variation_id = request.POST.get('variation_id')
        product_id= request.POST.get('product_id')
        print(product_id)
        product= Product.objects.get(id=product_id)
        # try:
        #     cart = Cart.objects.get(user=request.user, product_id=product_id, variation_id=variation_id)
        #     cart.quantity = quantity
        #     cart.save()
        # except :
        #     cart = Cart.objects.create(
        #         quantity=quantity,
        #         variation_id=variation_id,
        #         product_id=product_id,
        #         user=request.user
        #     ) 
        cart, is_created = Cart.objects.get_or_create(user=request.user, product_id=product_id, variation_id=variation_id)
        """get_or_create() : Either it will create object with kwargs or fetch object with given kwargs """
        cart.quantity = quantity
        cart.save()

        return redirect('ProductDetails', product_slug=product.slug)
    return redirect('home_page')


def my_cart_view(request):
  cart_products=Cart.objects.filter(user=request.user)
  sub_total = 0
  shipping = 50
  for cart_product in cart_products:
     cart_product.sub_total = cart_product.product.price * cart_product.quantity
     print(cart_product.sub_total)
     sub_total=sub_total + cart_product.sub_total
     grand_total = sub_total + shipping
  context={
     'cart_products' : cart_products,
     'sub_total' : sub_total,
     'grand_total' : grand_total,
     'shipping': shipping

  }
  return render(request, 'cart/my_cart_view.html', context)

def delete_cart_view_item(request, cart_id):
   try :
      Cart.objects.get(id=cart_id).delete()
   except Cart.DoesNotExist:
      pass
   return redirect('my_cart_view')   

def checkout(request):
   if request.method=="POST":
    """Form Handle"""
    pass
   return render(request, 'cart/checkout.html')