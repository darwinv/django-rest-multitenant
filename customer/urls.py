from django.urls import path
from . import views

urlpatterns = [

    path('customer/', views.CustomerCreateView.as_view(),
         name='create_customer'),

]
