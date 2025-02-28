# ContactsApp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Contact
from .forms import ContactForm
from django.db.models import Q
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer


# List all contacts
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'ContactsApp/contact_list.html', {'contacts': contacts})

# Create a new contact
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'ContactsApp/contact_form.html', {'form': form})

# Update an existing contact
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'ContactsApp/contact_form.html', {'form': form})

# Delete a contact
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'DELETE':  # Corrected to DELETE
        contact.delete()
        return HttpResponse("")  # Return an empty response for HTMX
    return render(request, 'ContactsApp/contact_confirm_delete.html', {'contact': contact})

# API endpoint for contacts
def contact_api(request):
    contacts = Contact.objects.all().values()
    return JsonResponse(list(contacts), safe=False)

# Search contacts
def contact_search(request):
    query = request.GET.get('q', '')  # Add default value
    if query:
        contacts = Contact.objects.filter(
            Q(name__icontains=query) |
            Q(address__icontains=query) |
            Q(phone_number__icontains=query)
        )
    else:
        contacts = Contact.objects.all()
    return render(request, 'ContactsApp/contact_list_partial.html', {'contacts': contacts})

# List and create contacts
class ContactListCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# Retrieve, update, and delete contacts
class ContactRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer