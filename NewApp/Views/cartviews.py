from django.shortcuts import render,redirect
from NewApp.models import Banner_image,Product,Category,Cart,Wishlist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.http.response import JsonResponse

@login_required(login_url='accessdenied')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def Add_to_cart(request,cate,name,qty):
    category=Category.objects.get(urlname=cate)
    prod=Product.objects.all().get(category=category.id,name=name)
    cart=Cart.objects.all().filter(user=request.user)
    if qty == None:
        qty=0
    else:
        qty=qty
    if len(cart)==0:
        add=Cart(category=prod,quantity=qty,user=request.user)
        add.save()
        messages.info(request,'Product is added to cart')
    else:
        if Cart.objects.filter(category=prod,user=request.user):
            cc=Cart.objects.get(category=prod,user=request.user)
            cc.quantity+=qty
            cc.save()
            messages.info(request,'Product is added to cart')   
        else:
            add=Cart(category=prod,quantity=qty,user=request.user)
            add.save()
            messages.info(request,'Product is added to cart')
    return redirect(f"/collections/{cate}")

@login_required(login_url='accessdenied')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def Cartview(request):
    cart=Cart.objects.all().filter(user=request.user)
    if request.user.is_authenticated:
        wishlist=Wishlist.objects.all().filter(user=request.user)
    else:
        wishlist=[]
    context={
        'cart':cart,
        'wishlist':wishlist
    }
    return render(request,'Store\Layout\cart.html',context=context)

@login_required(login_url='accessdenied')
def UpdateCart(request):
    if request.method=="POST":
        prod=Product.objects.get(id=int(request.POST['prod_id']))
        if Cart.objects.filter(category=prod,user=request.user):
            cart=Cart.objects.all().get(category=prod,user=request.user)
            cart.quantity=int(request.POST['qty'])
            cart.save()
            return render(request,'Store\Layout\cart.html')
    return redirect('/')

@login_required(login_url='accessdenied')
def Remove(request):
    if request.method=="POST":
       prod=Product.objects.get(id=int(request.POST['prod_id']))
       Cart.objects.get(category=prod,user=request.user).delete()
       return render(request,'Store\Layout\cart.html')
    return redirect('/')

