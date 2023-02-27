from django.shortcuts import render,redirect
from NewApp.models import Banner_image,Product,Category,Cart,Wishlist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.http.response import JsonResponse



@login_required(login_url='accessdenied')
def WishList(request):
    if request.method == "POST":
        id=int(request.POST['id'])
        prod=Product.objects.get(id=id)
        prod_val=Product.objects.values().filter(id=id)
        prodval=list(prod_val)
        wishlist=Wishlist.objects.all().filter(user=request.user)
        checked=0
        if len(wishlist)==0:
            wish=Wishlist(category=prod,user=request.user)
            wish.save()
        else:
            if Wishlist.objects.filter(user=request.user,category=prod):
                checked+=1
            else:
                checked+=0
            if checked == 1:
                w=Wishlist.objects.filter(user=request.user,category=prod)
                w.delete()
                wishlist_json= Wishlist.objects.values().filter(user= request.user)
                wishlist=list(wishlist_json)
                return JsonResponse({'Status':'Removed from wishlist','checked':checked})
            else:
                wish=wish=Wishlist(category=prod,user=request.user)
                wish.save()
        # wishlist_json= Wishlist.objects.values().filter(user= request.user)
        # wishlist=list(wishlist_json)
        return JsonResponse({'Status':'Product is add to wishlist','checked':checked})
    return redirect('/')


def Removewishlist(request):
    if request.method=='POST':
        wishid=int(request.POST['id'])
        Wishlist.objects.get(id=wishid).delete()
        return JsonResponse({'Status':'Remove successful'})