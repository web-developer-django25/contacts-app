# ContactsApp/api_urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.ContactListCreate.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', views.ContactRetrieveUpdateDestroy.as_view(), name='contact-retrieve-update-destroy'),
]