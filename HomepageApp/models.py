from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

# class Users(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField(verbose_name='Email',max_length=255,unique=True,)
#     number = models.CharField(max_length=20, null=False)
#     password = models.CharField(max_length=50)

class VehicleOwner(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)

class GarageOwner(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)

vehicleType = (
    ('Car','Car'),
    ('Mini Bus','Mini Bus'),
    ('Bike','Bike'),
    ('Bicycle','Bicycle'),
    ('Bus','Bus'),
    ('Truck','Truck')
)

class Vehicle(models.Model):
    vehicle_owner = models.ForeignKey(VehicleOwner, on_delete=models.CASCADE)
    type = models.CharField(choices=vehicleType, default='choose one', max_length=30)
    vehicle_num = models.CharField(max_length=200, primary_key=True)

class Garage(models.Model):
    garage_owner = models.ForeignKey(GarageOwner, on_delete=models.CASCADE)
    garage_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200)
    description = models.TextField()
    area = models.CharField(max_length=200)
    available = models.CharField(max_length=2, default='1')
    space = models.CharField(max_length=200)
    hourlyprice = models.FloatField()
    monthlyprice = models.FloatField()
    dailyprice = models.FloatField()
    upload = models.FileField()

policy = (
    ('Hourly','Hourly'),
    ('Monthly','Monthly'),
    ('Daily','Daily')
)

# class Rentals(models.Model):
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
#     garage = models.ForeignKey(Garage, on_delete=models.CASCADE)
#     policy = models.CharField(choices=policy, default='choose one', max_length=30)
#     rental_date = models.DateTimeField(auto_now_add=True)

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewer = models.EmailField(max_length=50) 
    reviewed = models.EmailField(max_length=50)
    statement = models.TextField(max_length=250)
    publish_date = models.DateTimeField(auto_now_add=True)