from django.contrib import admin
from django.urls import path,include
from store.views import home
from store.views.signup import Signup
from store.views.login import Login,logout
from store.views.product import product_get,product_search
from store.views.customer import customer_get,customer_search,customer_add,customer_alter,customer_update
from store.views.sale import Sale,Salesave,test



urlpatterns = [
    path('',home,name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('product', product_get,name='product'),
    path('search_product', product_search),
    path('customer', customer_get,name='customer'),
    path('search_customer', customer_search),
    path('customer_add', customer_add),
    path('alt_cust/<int:id>', customer_alter),
    path('update_cust/<int:id>', customer_update),
    path('sale',Sale.as_view(),name="sale"),
    path('salesave',Salesave.as_view(),name="salesave"),
    path('test',test,name="test"),
]
