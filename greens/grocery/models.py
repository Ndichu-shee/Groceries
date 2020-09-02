from django.db import models
from django.contrib.auth.models import User

class Owner(models.Model):
    GENDERS = (
        ("m", "male"),
        ("f", "female")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDERS)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    id_number = models.IntegerField()
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.get_full_name()

class Customer(models.Model):
    GENDERS = (
        ("m", "male"),
        ("f", "female")
    )
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    gender= models.CharField(max_length=6, choices=GENDERS)
    phone_number=models.IntegerField()
    date_of_birth=models.DateField()
    id_number=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.user.get_full_name()

class ShippingAddress(models.Model):
    customer= models.OneToOneField(Customer, on_delete=models.CASCADE)
    address=models.CharField(max_length=30)
    notes=models.TextField()

    def __str__(self):
        return self.customer.get_full_name()

class Order(models.Model):

    order_number=models.IntegerField()
    date_palced=models.DateTimeField()
    status=models.CharField(max_length=30)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    delivery_time=models.DateTimeField()
    order_price=models.DecimalField(max_digits=20, decimal_places=4)
    shipping_cost=models.DecimalField(max_digits=20, decimal_places=4)
    totalPrice=models.DecimalField(max_digits=20, decimal_places=4)


    def __str__(self):
        return self.order()

class Product(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    supplier_price=models.DecimalField(max_digits=20, decimal_places=4)
    selling_price=models.DecimalField(max_digits=20, decimal_places=4)
    number_in_stock=models.IntegerField()

    def __str__(self):
     return self.title
