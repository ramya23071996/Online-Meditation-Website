from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('therapy/', views.therapy_view, name='therapy'),
    path('about/', views.about_view, name='about'),
    path('meditation/', views.meditation_view, name='meditation'),
    path('contact/', views.contact_view, name='contact'),
    path('trials/', views.trials_view, name='trials'),
    path('family/', views.family_view, name='family'),
    path('approach/', views.approach_view, name='approach'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('payment/', views.payment_view, name='payment'),
]