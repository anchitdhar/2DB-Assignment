from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.indexView, name='Index'),
    path('register/', views.registerView, name='registerView'),
    path('login/', views.loginView, name='login'),
    path('logout/', LogoutView.as_view(next_page='Index'), name='logout'),
]