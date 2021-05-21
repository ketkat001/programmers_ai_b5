from django.urls import path
from . import views


app_name = 'strock'

urlpatterns = [
    path('', views.home, name='home'),
    path('age/', views.age, name='age'),
    path('bmi/', views.bmi, name='bmi'),
    path('smoking/', views.smoking, name='smoking'),
]