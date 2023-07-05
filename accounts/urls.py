from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="LoginView"),
    path('logout', views.logout_view, name="logout_view"),
    path('registraion', views.RegistraionView.as_view(), name="RegistraionView"),
    path('profile', views.ProfileView.as_view(), name="ProfileView")
]
