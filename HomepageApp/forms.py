from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordChangeForm, PasswordResetForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from .models import Vehicle,Garage, Reviews, VehicleOwner, GarageOwner, Rentals
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation

vehicleType = (
    ('Car','Car'),
    ('Mini Bus','Mini Bus'),
    ('Bike','Bike'),
    ('Bicycle','Bicycle'),
    ('Bus','Bus'),
    ('Truck','Truck')
)
class RegistrationForm(UserCreationForm):
        email = forms.CharField(label="Email", required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email', 'style':'opacity:0.8'}))
        username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username', 'style':'opacity:0.8'}))
        password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password', 'style':'opacity:0.8'}))
        password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password', 'style':'opacity:0.8'}))
        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'Username', 'style':'opacity:0.8; color:black'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
    'class':'form-control', 'PlaceHolder':'Password', 'style':'opacity:0.8;'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
    'autofocus':True,'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
    'class':'form-control'}),help_text = password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
    'class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete':'email',
    'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
    'class':'form-control'}),help_text = password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
    'class':'form-control'}))

class GarageForm(forms.ModelForm):
    class Meta:
        model = Garage
        fields = ['address','description','area', 'space' ,'hourlyprice','monthlyprice','dailyprice','upload' ]
        widgets = {'address':forms.TextInput(attrs={'class':'form-control'}),
                    'area':forms.TextInput(attrs={'class':'form-control'}),
                    'space':forms.TextInput(attrs={'class':'form-control'}),
                    'description':forms.Textarea(attrs={'class':'form-control'}),
                    'hourlyprice':forms.TextInput(attrs={'class':'form-control'}),
                    'monthlyprice':forms.TextInput(attrs={'class':'form-control'}),
                    'dailyprice':forms.TextInput(attrs={'class':'form-control'}),
                    'upload':forms.FileInput(attrs={'class':'form-control'}),
}

class VehicleForm(forms.ModelForm):
    # vehicle_num = forms.CharField(label="Vehicle Number", required=True)
    # type = forms.ChoiceField(label="Vehicle Type", choices=[vehicleType])
    class Meta:
        model = Vehicle
        fields = ['vehicle_num', 'type']
        widgets = {'type':forms.Select(attrs={'class':'regDropDown'}),
                    'vehicle_num':forms.TextInput(attrs={'class':'form-control'}),
                    }

class VehicleOwnForm(forms.ModelForm):
    class Meta:
        model = VehicleOwner
        fields = ['number']
        widgets = {
                    'number':forms.TextInput(attrs={'class':'form-control'})
                    }
        
class GarageOwnForm(forms.ModelForm):
    class Meta:
        model = GarageOwner
        fields = ['number']
        widgets = {
                    'number':forms.TextInput(attrs={'class':'form-control'})
                    }

# class ReviewsForm(forms.ModelForm):
#     class Meta:
#         model = Reviews
#         fields = ['reviewer','reviewed','statement']
#         widgets = {'reviewer':forms.TextInput(attrs={'class':'form-control','PlaceHolder':'Email'}),
#                     'reviewed':forms.TextInput(attrs={'class':'form-control','PlaceHolder':'Email'}),
#                     'statement':forms.Textarea(attrs={'class':'form-control'})}


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rentals
        fields = ['vehicle','garage','policy']
        widgets = {'vehicle':forms.TextInput(attrs={'class':'form-control','placeholder':'Vehicle Owner Id'}),
                    'garage':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Garage Id'}),
                    'policy':forms.Select(attrs={'class':'regDropDown', 'style':'color:black;'}),
                    }

# class Logform(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)