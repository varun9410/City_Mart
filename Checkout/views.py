from django.shortcuts import render
from django.shortcuts import render, redirect
from Shop.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from cart.context_processor import cart_total_amount

@login_required(login_url="/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/")


@login_required(login_url="/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

@login_required(login_url='/login')
def cart_detail(request):
    total=cart_total_amount(request)
    return render(request,'templates/cart.html',total)
# Create your views here.
@login_required(login_url='login')
def checkout(request):
	return render(request,'templates/checkout.html')
