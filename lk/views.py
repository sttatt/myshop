from django.shortcuts import render
from order.models import Order
from django.shortcuts import redirect
# Create your views here.


def lk(request):
    if(request.user):
        return render(request, 'main/lk.html', )
    return redirect("main:auth")

def orders(request):
    if(request.user):
        orders = Order.objects.filter(client=request.user)
        return render(request, 'main/zak.html', {'orders':orders})
    return redirect("main:auth")
