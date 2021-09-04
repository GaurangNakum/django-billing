from django import forms
from django.shortcuts import render,redirect
from django.db.models import Q
from django.shortcuts import HttpResponse
from store.models.customer import Customer
from store.models.forms_cust import CustomerForm


def customer_get(request):
    customer = Customer.objects.all()
    return render(request,'customermaster.html',{'customer' : customer})

def customer_search(request):
    search_customer = request.POST['src_cust_name']
    customer = Customer.objects.filter(Q(name__icontains=search_customer)|Q(code__icontains=search_customer)|Q(contact__icontains=search_customer))
    return render(request,'customermaster.html',{'customer' : customer})

def customer_add(request):
    form  = CustomerForm(request.POST)
    form.save()
    return redirect('customer')

def customer_alter(request,id):
    if id:
        customer = Customer.objects.get(id=id)
    else:
        customer = Customer.objects.all()
    return render(request,'alt_cust.html',{'customer' : customer})
    
def customer_update(request,id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(request.POST, instance=customer)
    form.save()
    return redirect('/customer')