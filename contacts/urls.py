from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.ContactListView.as_view(), name='contact_list'),
    path('create/', views.ContactCreateView.as_view(), name='contact_create'),
    path('<int:pk>/', views.ContactDetailView.as_view(), name='contact_detail'),
    path('<int:pk>/update/', views.ContactUpdateView.as_view(), name='contact_update'),
    path('<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact_delete'),
    # HTMX endpoints
    path('search/', views.contact_search, name='contact_search'),
]