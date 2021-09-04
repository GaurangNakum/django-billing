from django.contrib import admin
from store.models import Product,Category
from store.models.employee import Employee
from store.models.customer import Customer



class AdminProduct(admin.ModelAdmin):
    list_display = ['name']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminEmployee(admin.ModelAdmin):
    list_display = ['first_name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Employee,AdminEmployee)
admin.site.register(Customer,AdminCustomer)
