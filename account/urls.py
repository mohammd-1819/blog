from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('email/verify', views.VerifyEmailView.as_view(), name='verify-email'),
    path('password/reset', views.PasswordResetRequest.as_view(), name='password-reset'),
    path('password/reset/verify', views.PasswordResetVerifyView.as_view(), name='password-reset-verify'),
    path('password/reset/confirm', views.PasswordConfirmView.as_view(), name='password-reset-confirm'),

]
