from django.db import models
# from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

class Users(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='Email',max_length=255,unique=True,)
    number = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=50)

class VehicleOwner(models.Model):
    users = models.OneToOneField(Users, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='Email',max_length=255,unique=True,)
    number = models.CharField(max_length=20)

class GarageOwner(models.Model):
    users = models.OneToOneField(Users, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='Email',max_length=255,unique=True,)
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
    garage_num = models.CharField(max_length=200, primary_key=True)
    address = models.CharField(max_length=200)
    description = models.TextField()
    area = models.CharField(max_length=200)
    available = models.CharField(max_length=200)
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

class Rentals(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE)
    policy = models.CharField(choices=policy, default='choose one', max_length=30)
    rental_date = models.DateTimeField(auto_now_add=True)

class Reviews(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    reviewer = models.EmailField(max_length=50) 
    reviewed = models.EmailField(max_length=50)
    statement = models.TextField(max_length=250)
    publish_date = models.DateTimeField(auto_now_add=True)

# #  Custom User Manager
# class UserManager(BaseUserManager):
#   def create_user(self, email, name, number, password=None, password2=None):
#       """
#       Creates and saves a User with the given email, name, tc and password.
#       """
#       if not email:
#           raise ValueError('User must have an email address')

#       user = self.model(
#           email=self.normalize_email(email),
#           name=name,
#           number=number,
#       )

#       user.set_password(password)
#       user.save(using=self._db)
#       return user

#   def create_superuser(self, email, name, number, password=None):
#       """
#       Creates and saves a superuser with the given email, name, tc and password.
#       """
#       user = self.create_user(
#           email,
#           password=password,
#           name=name,
#           number=number,
#       )
#       user.is_admin = True
#       user.save(using=self._db)
#       return user

# #  Custom User Model
# class User(AbstractBaseUser):
#   email = models.EmailField(
#       verbose_name='Email',
#       max_length=255,
#       unique=True,
#   )
#   name = models.CharField(max_length=200)
#   number = models.CharField(max_length=200)
#   is_active = models.BooleanField(default=True)
#   is_admin = models.BooleanField(default=False)
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)

#   objects = UserManager()

#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = ['name', 'number']

#   def __str__(self):
#       return self.email

#   def has_perm(self, perm, obj=None):
#       "Does the user have a specific permission?"
#       # Simplest possible answer: Yes, always
#       return self.is_admin

#   def has_module_perms(self, app_label):
#       "Does the user have permissions to view the app `app_label`?"
#       # Simplest possible answer: Yes, always
#       return True

#   @property
#   def is_staff(self):
#       "Is the user a member of staff?"
#       # Simplest possible answer: All admins are staff
#       return self.is_admin








# class Vehicle(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     name = models.CharField(max_length=200)
#     type = models.CharField(choices=vehicleType, default='choose one', max_length=30)
#     vehiclenum = models.CharField(max_length=200)

#     def __str__(self):
#         return str(self.user)

# class Garage(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     name = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#     description = models.TextField()
#     hourlyprice = models.FloatField()
#     monthlyprice = models.FloatField()
#     dailyprice = models.FloatField()
#     upload = models.FileField()

#     def __str__(self):
#         return str(self.user)



# class rentals(models.Model):
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
#     garage = models.ForeignKey(Garage, on_delete=models.CASCADE)
#     policy = models.CharField(choices=policy, default='choose one', max_length=30)
#     rental_date = models.DateTimeField(auto_now_add=True)

# class Reviews(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     reviewer = models.EmailField(max_length=50) 
#     reviewed = models.EmailField(max_length=50)
#     statement = models.TextField(max_length=250)
#     publish_date = models.DateTimeField(auto_now_add=True)

# class Customer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.TextField(max_length=50)
#     email = models.EmailField(max_length=50) 
#     number = models.EmailField(max_length=50)