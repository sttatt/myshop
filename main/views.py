from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from cart.forms import CartAddProductForm
from order.models import Order


# Create your views here.
def index(request):
    return render(request,'main/index.html',{})

def products(request):
    products_list = Product.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request, 'main/tov.html', {"products_list": products_list,
                                             "cart_product_form":cart_product_form})

def about(request):
    return render(request, 'main/omag.html',{})

def contacts(request):
    return render(request, 'main/cont.html')

@csrf_exempt
def registration(request):
    if(request.method == "POST"):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            username = form.cleaned_data['email']
            pasword = form.cleaned_data['password']
            user = User.objects.create_user(username,'',pasword)
            user.first_name = name
            user.last_name = surname
            user.save()
            auth_login(request, user)
            return HttpResponseRedirect('/index')
        else:
            return HttpResponse('failed')
    else:
        form = RegistrationForm
        return render(request, 'main/reg.html', {'form':form})

@csrf_exempt
def auth(request):
    if(request.method == 'POST'):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                print("456")
                auth_login(request, user)
                return HttpResponseRedirect('/index')
            else:
                print(123)
                return HttpResponse('invalid login')

    else:
        form = LoginForm()
    return render(request, 'main/auth.html', {'form': form})

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/index')




