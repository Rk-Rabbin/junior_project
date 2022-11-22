from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordChangeForm, PasswordResetForm
from django.utils.translation import gettext, gettext_lazy as _
from .models import Vehicle, Users, Garage, Reviews, Rentals
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation

# vehicleType = (
#     ('Car','Car'),
#     ('Mini Bus','Mini Bus'),
#     ('Bike','Bike'),
#     ('Bicycle','Bicycle'),
#     ('Bus','Bus'),
#     ('Truck','Truck')
# )
# # class RegistrationForm(UserCreationForm):
# #     name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'Name', 'style':'opacity:0.7;'}))
# #     email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email', 'style':'opacity:0.7'}))
# #     mobilenumber = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'MobileNumber', 'style':'opacity:0.7'}))
# #     password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password', 'style':'opacity:0.7'}))
# #     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password', 'style':'opacity:0.7'}))
# #     class Meta:
# #         model = User
# #         fields =['name', 'email', 'mobilenumber', 'password1', 'password2']

#   widgets = {'vehicle':forms.TextInput(attrs={'class':'form-control'}),
#                     'garage':forms.TextInput(attrs={'class':'form-control'}),
#                     'policy':forms.Select(attrs={'class':'regDropDown', 'style':'color:black;'}),
#                     }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email', 'style':'opacity:0.7'}),
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Username', 'style':'opacity:0.7'}),
            'number' : forms.TextInput(attrs={'class':'form-control','placeholder':'PhoneNumber', 'style':'opacity:0.7'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password', 'style':'opacity:0.7'}),
            }
    

# # class LoginForm(AuthenticationForm):
# #     username = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'PlaceHolder':'Email', 'style':'opacity:0.7; color:black'}))
# #     password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
# #     'class':'form-control', 'PlaceHolder':'Password', 'style':'opacity:0.7;'}))

# class MyPasswordChangeForm(PasswordChangeForm):
#     old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
#     'autofocus':True,'class':'form-control'}))
#     new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
#     'class':'form-control'}),help_text = password_validation.password_validators_help_text_html())
#     new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
#     'class':'form-control'}))

# class MyPasswordResetForm(PasswordResetForm):
#     email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete':'email',
#     'class':'form-control'}))

# class MySetPasswordForm(SetPasswordForm):
#     new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
#     'class':'form-control'}),help_text = password_validation.password_validators_help_text_html())
#     new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
#     'class':'form-control'}))

# class GarageForm(forms.ModelForm):
#     class Meta:
#         model = Garage
#         fields = ['name','address','description','hourlyprice','monthlyprice','dailyprice','upload' ]
#         widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
#                     'address':forms.TextInput(attrs={'class':'form-control'}),
#                     'description':forms.Textarea(attrs={'class':'form-control'}),
#                     'hourlyprice':forms.TextInput(attrs={'class':'form-control'}),
#                     'monthlyprice':forms.TextInput(attrs={'class':'form-control'}),
#                     'dailyprice':forms.TextInput(attrs={'class':'form-control'}),
#                     'upload':forms.FileInput(attrs={'class':'form-control'}),
# }

# class VehicleForm(forms.ModelForm):
#     class Meta:
#         model = Vehicle
#         fields = ['name','type', 'vehiclenum']
#         widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
#                     'vehiclenum':forms.TextInput(attrs={'class':'form-control'}),
#                     'vehicletype':forms.Select(attrs={'class':'regDropDown'})
#                     }

# class ReviewsForm(forms.ModelForm):
#     class Meta:
#         model = Reviews
#         fields = ['reviewer','reviewed','statement']
#         widgets = {'reviewer':forms.TextInput(attrs={'class':'form-control','PlaceHolder':'Email'}),
#                     'reviewed':forms.TextInput(attrs={'class':'form-control','PlaceHolder':'Email'}),
#                     'statement':forms.Textarea(attrs={'class':'form-control'})}


# class RentalForm(forms.ModelForm):
#     class Meta:
#         model = rentals
#         fields = ['vehicle','garage','policy']
#         widgets = {'vehicle':forms.TextInput(attrs={'class':'form-control'}),
#                     'garage':forms.TextInput(attrs={'class':'form-control'}),
#                     'policy':forms.Select(attrs={'class':'regDropDown', 'style':'color:black;'}),
#                     }

# class Logform(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)