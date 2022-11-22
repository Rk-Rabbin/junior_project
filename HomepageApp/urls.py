from django.urls import path, include
from . import views
from .forms import MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm, LoginForm
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LandingPage , name='LandingPage'),
    # path('garagelist/', views.garagelist , name='garagelist'),
    # path('log2/', views.Log2Page , name='log2'),
    path('home/', views.HomePage , name='home'),
    path('profile/', views.ProfilePage , name='profile'),
    # # path('userprofile/', views.UserProfileView.as_view(), name='userprofile'),
    # path('profile/', views.UserProfile , name='profile'),
    path('registration/',views.RegistrationView.as_view(), name='registration'),
    # path('review/',views.ReviewView.as_view(), name='review'),
    path('vehicle/',views.VehicleView.as_view(), name='vehicle'),
    # path('rent/',views.RentalView.as_view(), name='rent'),
    # path('garagereg/',views.GarageView.as_view(), name='garagereg'),
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
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)