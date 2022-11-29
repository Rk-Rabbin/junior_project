from django.urls import path, include
from . import views
from .forms import MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm, LoginForm
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LandingPage , name='LandingPage'),
    path('home/', views.HomePage , name='home'),
    path('profile/', views.ProfilePage , name='profile'),
    path('search/', views.search_view , name='search'),
    path('mygarage/', views.mygarage , name='mygarage'),
    path('myvehicle/', views.myvehicle , name='myvehicle'),
    path('rent/<garage_id>',views.rent_view, name='rent'),
    path('updategarage/<garage_id>', views.updategarage , name='updategarage'),
    path('updatevehicle/<vehicle_num>', views.updatevehicle , name='updatevehicle'),
    path('del_vehicle/<vehicle_num>', views.del_vehicle , name='del_vehicle'),
    path('del_garage/<garage_id>', views.del_garage , name='del_garage'),
    path('registration/',views.RegistrationView.as_view(), name='registration'),
    path('garage-reg/',views.GarageRegView.as_view(), name='garage-reg'),
    path('vehicle-reg/',views.VehicleRegView.as_view(), name='vehicle-reg'),
    # path('review/',views.ReviewView.as_view(), name='review'),
    path('vehicle-owner/',views.VehicleOwnView.as_view(), name='vehicleown'),
    path('garage-owner/',views.GarageOwnView.as_view(), name='garageown'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='Homepage/login.html', authentication_form=LoginForm), name='login'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='Homepage/changepassword.html',
    form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='changepassword'),

    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='Homepage/passwordchangedone.html'),name='passwordchangedone'),

    path('logout/', auth_views.LogoutView.as_view(next_page='LandingPage'), name='logout'),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='Homepage/password_reset.html', form_class=MyPasswordResetForm),
    name='password_reset'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='Homepage/password_reset_done.html'),
    name='password_reset_done'),

    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='Homepage/password_reset_complete.html'),
    name='password_reset_complete'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='Homepage/password_reset_confirm.html',
    form_class=MySetPasswordForm), name='password_reset_confirm'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)