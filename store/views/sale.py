import django
from store.views import customer
from django import forms
from django.shortcuts import render,redirect
from django.db.models import Q
from django.shortcuts import HttpResponse
from store.models.product import Product
from store.models.customer import Customer
from django.views import View
from django.http import JsonResponse
import json


class Sale(View):
    def post(self , request):
        item_srno = request.POST.get('item_srno')
        srno = (request.POST.get('srno'))
        itemid = request.POST.get('itemid')
        itemname = request.POST.get('itemname')
        qty = request.POST.get('qty')
        rate = request.POST.get('rate')
        amount = request.POST.get('amount')
        
        cart = request.session.get('cart')

        if item_srno:
            #print(item_srno)
            del cart[item_srno]
            request.session['cart'] = cart
            i = 0
            cart2 = cart
            cart = {}
            for (key, value) in cart2.items():
                i = i +1
                cart[i] = cart2[key]
                
            request.session['cart'] = cart


            
        if srno and itemid :
            if cart:
                cart[srno]  = [itemid,itemname, qty, rate,amount]
            else:
                cart={}
                cart[srno]  = [itemid,itemname, qty, rate,amount]
            request.session['cart'] = cart
        
        #cart={}
        #request.session['cart'] = cart
        
        return redirect('sale')
        

    def get(self,request):
        product = Product.objects.all()
        customer = Customer.objects.all()

        data = {}
        data['product'] = product
        data['customer'] = customer
        
        return render(request,'sale.html',data)

class Salesave(View):
    def post(self , request):
        print (request.POST)
        custid =  request.POST.get('custid')
        custname =  request.POST.get('custname')
        sale = request.session.get('sale')
        if sale:
            pass
        else:
            sale={}
        sale= ["saleno",custid,custname]
        
        request.session['sale'] = sale
        
        print(sale)
        return redirect('sale')

def test(request):
    if not request.is_ajax() or not request.method=='POST':
        return HttpResponseNotAllowed(['POST'])

    request.session['sale'] = 'myvalue'
    print(request.session('mykey'))
    return HttpResponse('ok')