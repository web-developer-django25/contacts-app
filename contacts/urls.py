from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    # Contact URLs
    path('', views.ContactListView.as_view(), name='contact_list'),
    path('contact/<int:pk>/', views.ContactDetailView.as_view(), name='contact_detail'),
    path('contact/add/', views.ContactCreateView.as_view(), name='contact_create'),
    path('contact/<int:pk>/edit/', views.ContactUpdateView.as_view(), name='contact_update'),
    path('contact/<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact_delete'),
    path('contact/search/', views.contact_search, name='contact_search'),

    # Category URLs
    path('category/add/', views.CategoryCreateView.as_view(), name='category_create'),
]