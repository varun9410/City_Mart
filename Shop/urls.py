from django.urls import path
from Shop import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop',views.shop,name='shop'),
    path('shop/<str:category>',views.shop_by_category,name='shop_by_category'),
    path('detail/<str:product_id>',views.detail,name='detail'),
    path('contact',views.contact,name='contact'), 
    path('product',views.product,name='product'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('find_product',views.find_product,name='find_product'),
    #path('test',views.test,name='test')
]