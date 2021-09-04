from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=150)
    code =  models.CharField(max_length=20,blank=True)
    address =  models.CharField(max_length=250,blank=True)
    city = models.CharField(max_length=100,blank=True)    
    contact = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return  self.name
        
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    @staticmethod
    def get_all_customer():
        return Customer.objects.all()

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return  False
