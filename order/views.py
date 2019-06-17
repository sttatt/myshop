from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import TempProduct
from .forms import OrderCreateForm
from cart.cart import Cart


def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            if(request.user):
                order.client = request.user
                order.save()
            for item in cart:
                TempProduct.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'main/thanks.html', {'order': order})

    form = OrderCreateForm()
    return render(request, 'main/oform.html', {'cart': cart,
                                                        'form': form})