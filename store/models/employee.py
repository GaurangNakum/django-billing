from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return  self.first_name
        
    def register(self):
        self.save()

    @staticmethod
    def get_employee_by_email(email):
        try:
            return Employee.objects.get(email=email)
        except:
            return False

    @staticmethod
    def get_all_employee():
        return Employee.objects.all()

    def isExists(self):
        if Employee.objects.filter(email = self.email):
            return True

        return  False
