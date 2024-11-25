from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class Products(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey('auth.User',on_delete = models.CASCADE)
    product = models.ForeignKey(Products,on_delete = models.CASCADE) 
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.product.name} x {self.quantity}"
    

