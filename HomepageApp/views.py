from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .forms import RegistrationForm, VehicleOwnForm, LoginForm, GarageOwnForm, GarageForm, VehicleForm
# from .forms import RegistrationForm, GarageForm, VehicleForm, RentalForm, ReviewsForm, Logform
from .models import User, Garage, Reviews, Vehicle, VehicleOwner, GarageOwner
# from .forms import MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required


# Create your views here.

def LandingPage(request):
    return render(request, 'Homepage/LandingPage.html')

def ProfilePage(request):
    usr = request.user
    return render(request, 'Homepage/profile.html',{'usr':usr,'active':'btn-warning'})

def UserProfile(request):
    return render(request, 'Homepage/userprofile.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
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


class GarageRegView(View):
    def get(self,request):
        form = GarageForm()
        return render(request, 'Homepage/garage.html' , {'form':form})
    def post(self, request):
        form = GarageForm(request.POST, request.FILES)
        if form.is_valid():
            usr = request.user
            uid = usr.id
            try:
                g_own = GarageOwner.objects.get(users_id=uid)
                gid = g_own.id
            except GarageOwner.DoesNotExist:
                g_own = None
                messages.success(request, 'Sorry')
                return render(request, 'Homepage/garage.html' , {'form':form, 'message':messages})
            address = form.cleaned_data['address']
            description = form.cleaned_data['description']
            area = form.cleaned_data['area']
            space = form.cleaned_data['space']
            hourlyprice = form.cleaned_data['hourlyprice']
            dailyprice = form.cleaned_data['dailyprice']
            monthlyprice = form.cleaned_data['monthlyprice']
            upload = form.cleaned_data['upload']
            reg = Garage(garage_owner_id=gid, address=address, description=description, area=area, space=space, hourlyprice=hourlyprice,
            dailyprice=dailyprice, monthlyprice=monthlyprice, upload=upload)
            reg.save()
            messages.success(request, 'Congratulations!! Successfully Registered your garage')
        return render(request, 'Homepage/garage.html' , {'form':form})

class VehicleRegView(View):
    def get(self,request):
        return render(request, 'Homepage/vehicle.html')
    def post(self, request):
        if request.method == "POST":
            usr = request.user
            uid = usr.id
            try:
                v_own = VehicleOwner.objects.get(users_id = uid)
                vid = v_own.id
            except VehicleOwner.DoesNotExist:
                v_own = None
                messages.success(request, 'Congratulations!! Successfully Registered your vehicle')
                return render(request, 'Homepage/vehicleOwnReg.html' , {'message':messages})
            vehicle_num = request.POST['vnum']
            type = request.POST['type']
            reg = Vehicle(vehicle_owner_id=vid, vehicle_num=vehicle_num, type=type)
            reg.save()
            messages.success(request, 'Congratulations!! Successfully Registered your vehicle')
            return render(request, 'Homepage/vehicle.html', {'message':messages})

def mygarage(request):
    usr = request.user
    uid = usr.id
    try:
        g_own = GarageOwner.objects.get(users_id=uid)
        gid = g_own.id
        mg = Garage.objects.filter(garage_owner=gid)
        return render(request, 'Homepage/mygarage.html',{'mg':mg})
    except GarageOwner.DoesNotExist:
        return render(request, 'Homepage/mygarage.html',{'mg':mg})


def myvehicle(request):
    usr = request.user
    uid = usr.id
    try:
        v_own = VehicleOwner.objects.get(users_id = uid)
        vid = v_own.id
        mv = Vehicle.objects.filter(vehicle_owner=vid)
        return render(request, 'Homepage/myvehicle.html',{'mv':mv})
    except:
        return render(request, 'Homepage/myvehicle.html',{'mv':mv})


def updategarage(request, garage_id):
    if request.method == 'POST':
        try:
            dl = Garage.objects.get(garage_id=garage_id)
            fm = GarageForm(request.POST, instance=dl)
            if fm.is_valid():
                fm.save()
                return redirect('mygarage')
        except:
            messages.warning("sorry, could not update garage information!!")
            return render(request, 'Homepage/mygarage.html',{'message':messages})
    else:
        dl = Garage.objects.get(garage_id=garage_id)
        fm = GarageForm(instance=dl)
    return render(request, 'Homepage/updategarage.html', {'form':fm})



def updatevehicle(request, vehicle_num):
    if request.method == 'POST':
        try:
            dl = Vehicle.objects.get(vehicle_num=vehicle_num)
            fm = VehicleForm(request.POST, instance=dl)
            if fm.is_valid():
                fm.save()
                return redirect('myvehicle')
        except:
            messages.warning("sorry, could not update garage information!!")
            return render(request, 'Homepage/myvehicle.html',{'message':messages})
    else:
        dl = Vehicle.objects.get(vehicle_num=vehicle_num)
        fm = VehicleForm(instance=dl)
    return render(request, 'Homepage/updatevehicle.html', {'form':fm})



def del_vehicle(request, vehicle_num):
    if request.method == 'POST':
        try:
            dl = Vehicle.objects.get(vehicle_num=vehicle_num)
            dl.delete()
            return render(request, 'Homepage/myvehicle.html')
        except:
            messages.warning("could not delete vehicle!!")
            return render(request, 'Homepage/myvehicle.html',{'message':messages})


def del_garage(request, garage_id):
    if request.method == 'POST':
        try:
            dl = Garage.objects.get(garage_id=garage_id)
            dl.delete()
            return render(request, 'Homepage/mygarage.html')
        except:
            messages.warning("could not delete garage!!")
            return render(request, 'Homepage/mygarage.html',{'message':messages})


def search_view(request):
    search = request.GET['search']
    garages = Garage.objects.filter(area__icontains=search)
    params = {'garages':garages}
    return render(request,'Homepage/garagelist.html', params)