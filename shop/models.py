from django.db import models

# Create your models here.

class productmodel(models.Model):
    Title= models.CharField(max_length=225,name='TITLE',null=False)
    Description=models.TextField(max_length=500,name='DESCRIPTION',null=True)
    Price=models.IntegerField(name="PRICE",null=False)
    Rating=models.IntegerField(name='RATINGS',default=0)
    imagepath=models.ImageField(name="IMAGE",upload_to='product_images/', null=True)
    Product_Category=models.CharField(name="PRODUCT_CATEGORY",max_length=500, null=True)
    
