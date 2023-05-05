from django.shortcuts import render
from .models import * 

def shopping(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'shopapp/shopping.html', context)

def cart(request):
	context = {}
	return render(request, 'shopapp/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'shopapp/checkout.html', context)