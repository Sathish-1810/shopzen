from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
   
    path('products/', views.product_list, name='product_list'),
    path('aboutus/' , views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name = 'contactus'),
    
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/',views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('payment/', views.payment_page, name='payment_page'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('',views.home, name='category_list'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/count/', views.cart_item_count, name='cart_item_count'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
