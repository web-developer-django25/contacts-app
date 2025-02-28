# ContactsApp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.contact_search, name='contact_search'),
    path('', views.contact_list, name='contact_list'),
    path('create/', views.contact_create, name='contact_create'),
    path('update/<int:pk>/', views.contact_update, name='contact_update'),
    path('delete/<int:pk>/', views.contact_delete, name='contact_delete'),
    path('api/', views.contact_api, name='contact_api'),
    path('search/', views.contact_search, name='contact_search'),

]

