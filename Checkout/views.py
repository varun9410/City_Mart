from django.shortcuts import render
from django.shortcuts import render, redirect
from Shop.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from cart.context_processor import cart_total_amount
from .models import Order, OrderItem
from Shop.models import Profile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
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

@login_required(login_url='login')
def checkout(request):
    profile=Profile.objects.filter(user_id=request.user)
    total = cart_total_amount(request)
    total = total['cart_total_amount']+100
    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            total_amount=total,  
        )
        cart=request.session.get('cart')
        for key,item in cart.items():
            product_id = item['product_id']
            quantity = item['quantity']
            price = item['price']
            product = get_object_or_404(Product, id=product_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=price,
                
            )
            cart = Cart(request)
            cart.clear()
        return render(request,'order_success.html')

    return render(request, 'checkout.html', {'total': total,'profile':profile})
