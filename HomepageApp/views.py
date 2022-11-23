from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistrationForm, VehicleOwnForm, LoginForm, GarageOwnForm
# from .forms import RegistrationForm, GarageForm, VehicleForm, RentalForm, ReviewsForm, Logform
from .models import User, Garage, Reviews, Vehicle, VehicleOwner, GarageOwner
# from .forms import MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.cache import cache_control


# Create your views here.

def LandingPage(request):
    return render(request, 'Homepage/LandingPage.html')

def ProfilePage(request):
    usr = request.user
    return render(request, 'Homepage/profile.html',{'usr':usr,'active':'btn-warning'})

def garagelist(request):
    return render(request,'Homepage/garagelist.html')

def UserProfile(request):
    return render(request, 'Homepage/userprofile.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def HomePage(request):
    if request.user is not None:
            return render(request, 'Homepage/home.html')
    else:
        return redirect('LoginView')

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
        

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def LoginView(request):
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


class VehicleOwnView(View):
    def get(self,request):
        form = VehicleOwnForm()
        return render(request, 'Homepage/vehicleOwnReg.html' , {'form':form})
    def post(self, request):
        form = VehicleOwnForm(request.POST)
        if form.is_valid():
            usr = request.user
            uid = usr.id
            number = form.cleaned_data['number']
            reg = VehicleOwner(users_id=uid, number=number)
            reg.save()
            messages.success(request, 'Congratulations!! Successfully Registered')
        return render(request, 'Homepage/vehicleOwnReg.html' , {'form':form})

class GarageOwnView(View):
    def get(self,request):
        form = GarageOwnForm()
        return render(request, 'Homepage/garageOwnReg.html' , {'form':form})
    def post(self, request):
        form = GarageOwnForm(request.POST)
        if form.is_valid():
            usr = request.user
            uid = usr.id
            number = form.cleaned_data['number']
            reg = GarageOwner(users_id=uid, number=number)
            reg.save()
            messages.success(request, 'Congratulations!! Successfully Registered')
        return render(request, 'Homepage/garageOwnReg.html' , {'form':form})



