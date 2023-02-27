from django.shortcuts import render,redirect
from NewApp.models import Banner_image,Product,Category,Cart,Wishlist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.http.response import JsonResponse
from  django.contrib.auth import authenticate

# Create your views here.

def home(request):
    banner=Banner_image.objects.all()
    if request.user.is_authenticated:
        wishlist=Wishlist.objects.all().filter(user=request.user)
    else:
        wishlist=[]
    context={
        'banner':banner,
        'wishlist':wishlist
    }
    return render(request,'Store\Layout\home.html',context=context)

def Collections(request):
    ourCollections=Category.objects.all()
    if request.user.is_authenticated:
        wishlist=Wishlist.objects.all().filter(user=request.user)
    else:
        wishlist=[]
    context={
        'ourCollections':ourCollections,
        'wishlist':wishlist
    }
    return render(request, 'Store\Layout\collections.html',context)

def Collectionsview(request,name):
    if Category.objects.filter(urlname=name):
        category=Category.objects.all().get(urlname=name)
        products=Product.objects.all().filter(category=category)
        if request.user.is_authenticated:
            wishlist=Wishlist.objects.all().filter(user=request.user)
        else:
            wishlist=[]
        context={
            "products":products,
            'category':category,
            'wishlist':wishlist
        }
        # print(Product.objects.filter(category=name))
    return render(request,'Store\Layout\Product\product.html',context)


def Productview(request,cate,prod):
    categoy_name= Category.objects.get(urlname=cate)
    if Category.objects.filter(urlname=cate):
        if Product.objects.filter(category=categoy_name.id,name=prod):
            categoryname=Category.objects.get(urlname=cate)
            itemname=Product.objects.get(category=categoryname,name=prod)
            if request.user.is_authenticated:
                wishlist=Wishlist.objects.all().filter(user=request.user)
                checked=0
                if Wishlist.objects.filter(user=request.user,category=itemname):
                    checked+=1
                else:
                    checked+=0 
            else:
                wishlist=[]
                checked=0
            context={
                'itemname':itemname,
                'categoryname':categoryname,
                'wishlist':wishlist,
                'checked':checked,
            }
            return render(request,'Store\Layout\Product\productview.html', context)


def Accessdenied(request):
    return render(request,'Store/accessdenied.html')


