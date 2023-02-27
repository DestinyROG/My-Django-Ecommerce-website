from django.shortcuts import render,redirect
from NewApp.models import Banner_image,Product,Category,Cart,Wishlist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.http.response import JsonResponse

@login_required(login_url='accessdenied')
@cache_control(no_chache=True,must_revalidate=True,no_store=True)
def Checkout(request):
    if request.user.is_authenticated:
        wishlist=Wishlist.objects.all().filter(user=request.user)
    else:
        wishlist=[]
    row_cart=Cart.objects.filter(user=request.user)
    cartitem=[]
    for item in row_cart:
        if item.quantity>item.category.quantity:
            pass
        else:
            if item.quantity==0:
                pass
            else:
                cartitem.append(item)
    grand_total=0
    for i in cartitem:
        grand_total+=(i.quantity*i.category.selling_price)
    context={
        'cartitem':cartitem,
        'grand_total':grand_total,
        'wishlist':wishlist,
    }
    return render(request,'Store\Layout\checkout.html',context)