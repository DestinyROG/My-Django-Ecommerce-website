from django.urls import path
from NewApp.Views import views,cartviews,wishlistviews,checkoutviews

urlpatterns=[
    path('',views.home, name='home'),
    path('collections/',views.Collections, name='collections'),
    path('collections/<str:name>',views.Collectionsview, name= 'collectionsview'),
    path('collections/<str:cate>/<str:prod>',views.Productview, name='productview'),


    path('addToCart/<str:cate>/<str:name>/<int:qty>',cartviews.Add_to_cart,name="addToCart"),
    path('cart',cartviews.Cartview,name='cart'),
    path('update-cart',cartviews.UpdateCart,name='update-cart'),
    path('remove',cartviews.Remove,name='remove'),

    path('accessdenied',views.Accessdenied,name='accessdenied'),

    path('wishlist',wishlistviews.WishList,name='wishlist'),
    path('removewishlist',wishlistviews.Removewishlist,name='removewishlist'),

    path('checkout',checkoutviews.Checkout, name='checkout')
]