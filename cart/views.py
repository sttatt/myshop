from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from cart.cart import Cart
from main.models import Product
from django.shortcuts import render,get_object_or_404, redirect
from cart.forms import CartAddProductForm

# Create your views here.

@csrf_exempt
@require_POST
def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                                  update_quantity=cd['update'])
    return redirect('main:products')

def CartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    for item in cart.cart.items():
        print(item)
    cart.remove(product)
    return redirect('cart:CartDetail')

def CartDetail(request):
    cart = Cart(request)
    for item in cart.cart.items():
        print(item)
    return render(request, 'main/cart.html', {'cart' : cart})