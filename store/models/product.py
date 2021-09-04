from django.db import models




class Category(models.Model):
    name =  models.CharField(max_length=100,null=False)
    code =  models.CharField(max_length=50,null=True , blank=True)

    def __str__(self):
        return  self.name

class Product(models.Model):
    name =  models.CharField(max_length=100,null=False)
    code =  models.CharField(max_length=50,null=True , blank=True)
    remark =  models.CharField(max_length=250,null=True , blank=True)
    mrp =  models.IntegerField(null=False,default=0)
    unit =  models.CharField(max_length=10,null=True , blank=True)
    rate =  models.IntegerField(null=False,default=0)
    cat_id = models.ForeignKey(Category,null = False, on_delete=models.CASCADE,default=1)
    #cat_id =  models.IntegerField(null=False,default=0)
    gst =  models.IntegerField(null=False,default=0)
    minq =  models.IntegerField(null=False,default=0)
    maxq =  models.IntegerField(null=False,default=0)
    image = models.ImageField(upload_to='uploads/products/')
    status =  models.BooleanField(default=False)

    def __str__(self):
        return  self.name

    

