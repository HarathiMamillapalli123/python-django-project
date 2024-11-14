
from django.urls import path
from .import views

urlpatterns = [
    path('chi/',views.home,name='home'),
    path('chinni/', views.chinni, name='chinni'),
    
]
