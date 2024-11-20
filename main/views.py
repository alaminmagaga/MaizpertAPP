from django.shortcuts import render
from store.utils import cookieCart,cartData,guestOrder

# Create your views here.

def index(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']


    context={'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'index.html' , context)

def about(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']


    context={'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'about.html' , context)

def services(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']


    context={'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'services.html' , context)
    

def sell(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']


    context={'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'sell.html' , context)
    

def storage(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']


    context={'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'storage.html' , context)

def market(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']


    context={'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'market.html' , context)


    
