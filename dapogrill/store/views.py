from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import *
from django.http import JsonResponse
import datetime
import json
from .utils import cookieCart, cartData, guestOrder



def home(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {'cartItems': cartItems}
    return render(request, 'store/home.html', context)
def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
   
    products = Product.objects.all()
    context = {'products':products ,'cartItems': cartItems}
    return render(request, 'store/store.html', context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
        
    context = {'items':items, 'order':order,'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items,'order':order,'cartItems': cartItems,'locations':LOCATIONS, 'payment_method':PAYMENT_METHOD}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action =='add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
   
    else:
        customer,order = guestOrder(request, data)
    
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
        order.order_status = "Order Processing"
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer = customer,
            order = order,
            full_address = data['shipping']['addressfull'],
            address = data['shipping']['address'],
            phone = data['shipping']['phone'],
            Payment_method = data['shipping']['Payment_method'], 
        )
    return JsonResponse('Payment Complete', safe=False)
    return render('home')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None and Admin.objects.filter(user=user).exists():
            auth.login(request, user)
            messages.success(request, 'You are now logged in ')
            return redirect('adminhome')
        else:
            messages.error(request, 'Invalid Credential')
            return redirect('adminlogin')
    else:
        return render(request, 'store/admin_login.html')

def adminhome(request):
    orders = Order.objects.filter(order_status = "Order Processing").order_by('-id')[:5]
    shipping = ShippingAddress.objects.all()
    customers = Customer.objects.all().order_by('-id')[:3]
    ordertotal = Order.objects.count()
    orderdelivered = Order.objects.filter(order_status='Order Received').count()
    orderprocessing = Order.objects.filter(order_status='Order Processing').count()
    if request.user.is_authenticated and Admin.objects.filter(user=request.user).exists():
        pass
    else:
        return redirect('adminlogin')
    context = {'orders': orders, 'customers':customers, 'ordertotal':ordertotal,'orderdelivered':orderdelivered, 'orderprocessing': orderprocessing}
    return render(request, 'store/admin_home.html', context)
def adminallorder(request):
    orders = Order.objects.all().order_by('-id')
    shipping = ShippingAddress.objects.all()
    customers = Customer.objects.all()[:3]
    ordertotal = Order.objects.count()
    orderdelivered = Order.objects.filter(order_status='Order Received').count()
    orderprocessing = Order.objects.filter(order_status='Order Processing').count()
    if request.user.is_authenticated and Admin.objects.filter(user=request.user).exists():
        pass
    else:
        return redirect('adminlogin')
    context = {'orders': orders, 'customers':customers, 'ordertotal':ordertotal,'orderdelivered':orderdelivered, 'orderprocessing': orderprocessing}
    return render(request, 'store/admin_allorder.html', context)

def adminhomeid(request, transaction_id):
    order = get_object_or_404(Order, pk=transaction_id)
    shipping = get_object_or_404(ShippingAddress, order=transaction_id)
    # total = Order.objects.all()
    orderitems = OrderItem.objects.filter(order_id = transaction_id)
    if request.user.is_authenticated and Admin.objects.filter(user=request.user).exists():
        pass
    else:
        return redirect('adminlogin')
    context = {'order': order , 'orderitems':orderitems, 'allstatus':ORDER_STATUS, 'shipping':shipping}
    return render(request, 'store/admin_homeid.html', context)


def adminchangestatus(request, transaction_id):
    order = get_object_or_404(Order, pk=transaction_id)
    order_by = Order.objects.get(id=order.id)
    new_status = request.POST.get('status')
    order_by.order_status = new_status
    order_by.save()
    if request.user.is_authenticated and Admin.objects.filter(user=request.user).exists():
        pass
    else:
        return redirect('adminlogin')
    context = {'order': order}
    return redirect('adminhome')

def productcreate(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        image = request.FILES['image']

        product, created = Product.objects.get_or_create(name=name, price=price, image=image)
        product.save()
        messages.success(request, 'New Product Added')
        return redirect('adminhome')
    else:
        return render(request, 'store/productUpdate.html')





