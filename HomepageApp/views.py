from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistrationForm, VehicleForm, LoginForm
# from .forms import RegistrationForm, GarageForm, VehicleForm, RentalForm, ReviewsForm, Logform
# from .models import User, Garage, Reviews, Vehicle, rentals, Customer
# from .forms import MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def LandingPage(request):
    return render(request, 'Homepage/LandingPage.html')

def garagelist(request):
    return render(request,'Homepage/garagelist.html')

def UserProfile(request):
    return render(request, 'Homepage/userprofile.html')

def HomePage(request):
    return render(request, 'Homepage/home.html')

class RegistrationView(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request, 'Homepage/register.html' , {'form':form})
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Congratulations!! Successfully Registered')
            except:
                messages.success(request, 'Sorry!! Could not be Registered, Try Again')
        return render(request, 'Homepage/register.html' , {'form':form})
        

def LoginView(request):
    # if request.user.is_authenticated:
    #     return render(request, 'Homeapp/home.html')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'Homeapp/home.html',{'user':user})
        else:
            messages.success(request, 'Something went wrong, Try Again')
            form = LoginForm()
            return render(request, 'Homepage/login.html', {'form':form, 'message':messages})
    else:
        form = LoginForm()
        return render(request, 'Homepage/login.html', {'form':form})


# class RentalView(View):
#     def get(self,request):
#         form = RentalForm()
#         return render(request, 'Homepage/rent.html' , {'form':form})
#     def post(self, request):
#         form = RentalForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Congratulations!! Successfully Registered')
#         return render(request, 'Homepage/rent.html' , {'form':form})

# class ReviewView(View):
#     def get(self,request):
#         form = ReviewsForm()
#         return render(request, 'Homepage/review.html' , {'form':form})
#     def post(self, request):
#         form = ReviewsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Congratulations!! Successfully Registered')
#         return render(request, 'Homepage/review.html' , {'form':form})

class VehicleView(View):
    def get(self,request):
        form = VehicleForm()
        return render(request, 'Homepage/vehicle.html' , {'form':form})
    def post(self, request):
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations!! Successfully Registered')
        return render(request, 'Homepage/vehicle.html' , {'form':form})

# class GarageView(View):
#     def get(self,request):
#         form = GarageForm()
#         return render(request, 'Homepage/garage.html' , {'form':form})
#     def post(self, request):
#         form = GarageForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Congratulations!! Successfully Registered')
#         return render(request, 'Homepage/garage.html' , {'form':form})



# def Log2Page(request):
#     if request.method == 'POST':
#         form = Logform(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data()
#             user = authenticate(request,username=cd['username'],password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request,user)
#                     return render(request,'Homapage/home.html')
#                 else:
#                     return HttpResponse("Inactive Account")
#             else:
#                 return HttpResponse("Invalid Login")
#     else:
#         form = Logform()
#         return render(request,'Homepage/login.html',{'form':form})
