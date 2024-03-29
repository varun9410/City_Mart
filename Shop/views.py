from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Product,Contact,Category,Review
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from kafka import KafkaProducer
import json
def index(request):
	page='Home'
	#send_data(page,request)
	if request.method=='POST':
		search_item=request.POST['search']
		product=Product.objects.filter(name__contains=search_item) | Product.objects.filter(sub_category__contains=search_item)
		product={'product':product}
		if product is not None:
			return render(request,'shop.html',product)
		else:
			messages.warning(request,'There no such product exists')
			return render(request,'shop.html')
	category=Category.objects.all()
	category={'category':category}
	#log_time_spent(request)
	return render(request, "index.html",category)

def shop(request):
	#page='shop'
	#send_data(page,request)
	product=Product.objects.all()
	product={'product':product}
	return render(request,'shop.html',product)
@login_required(login_url='/login')
def shop_by_category(request,category):
	print(category)
	product=Product.objects.filter(category=category)
	product={'product':product}
	return render(request,'shop.html',product)

@login_required(login_url='/login')
def detail(request,product_id):
	#page='product_id'
	#send_data(page,request)
	product=Product.objects.filter(id=product_id)
	review=Review.objects.filter(Product_id=product_id)
	context={'product':product,
	'review':review}
	product1=Product.objects.get(id=product_id)
	if request.method == "POST":
		review=Review()
		review.Product_id=product1
		review.User_id=request.user
		review.review=request.POST['review']
		review.save()
	return render(request,'detail.html',context)

def product(request):
	#page='product-page'
	#send_data(page,request)
	obj=Product.objects.all()
	obj={'obj':obj}
	return render(request,'product.html',obj)
# Authentication System
def register(request):
	#page='register'
	#send_data(page,request)
	if request.method=='POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		User_id=request.POST['User_id']
		Email=request.POST['email']
		password=request.POST['password1']
		password2=request.POST['password2']
		if password==password2:
			if User.objects.filter(username=User_id).exists():
			    messages.warning(request,'This User Id or Email already Exists')
			elif User.objects.filter(email=Email).exists():
				messages.warning(request,'This User Id or Email already Exists')
			else:
				user=User.objects.create_user(username=User_id,email=Email,password=password,first_name=first_name,last_name=last_name)
				user.save()
				return redirect('/')
		else:
			messages.warning(request,'please enter the same password ')	
	return render(request,'register.html')

def login(request):
	#page='login'
	#send_data(page,request)
	if request.method=='POST':
		User=request.POST['User_id']
		password=request.POST['password']
		user=authenticate(request,username=User,password=password)
		if user is not None:
			auth_login(request, user)
			if user.is_authenticated:
				return redirect('/')
		else:
			print('somthing went wrong')
	return render(request,'login.html')

@login_required(login_url='/login')
def logout(request):
	#page='logout'
	#send_data(page,request)
	auth_logout(request)
	return redirect('/')

# Contact form
def contact(request):
	#page='contact'
	#send_data(page,request)
	if request.method=='POST':
		contact=Contact()
		contact.Name= request.POST['name']
		contact.Email=request.POST['email']
		contact.Subject=request.POST['subject']
		contact.Message=request.POST['message']
		contact.save()
		print('success gfsef')
	return render(request,'contact.html')
import requests
from django.http import HttpResponse

def send_image_file(file):
    api_url = 'https://varun9410-psychic-eureka-x77p5q6rxqcv6x4-5000.preview.app.github.dev/find_product'  # Replace with your API endpoint URL

    # Prepare the data to be sent to the API endpoint
    files = {'image': file}

    # Send a POST request to the API endpoint
    response = requests.post(api_url, files=files)

    if response.status_code == 200:
        # Handle the API response
        api_response = response.json()
        # Process the response as needed
        return api_response

    # Return None or raise an exception if the request fails
    return None

def find_product(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')

        # Call the function to send the image file and retrieve the API response
        api_response = send_image_file(image_file)

        if api_response is not None:
            # Process the API response
            # ...
            print(api_response)
            return HttpResponse('Image processed successfully!')

    return HttpResponse('Image processing failed!')


##def product_by_category(request,category):
##	product=Product.objects.filter(category=category)
##	return render(request,'shop.html',product)
def log_time_spent(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        time_spent = data['time_spent']
        print("bbbbbbbbbbbbbb",time_spent)


import datetime
import json
from kafka import KafkaProducer

def send_data(page, request):
    data = request.META.get('REMOTE_ADDR')	
    time = datetime.datetime.now()

    kafka = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    endpoint = request.META.get('PATH_INFO')

    if request.user is not None:
        user = request.user
    else:
        user = 'null'

    kafka.send('store-data', {'user': str(user), 'ip': data, 'page': str(page), 'endpoint': endpoint, 'datetime': str(time)})

