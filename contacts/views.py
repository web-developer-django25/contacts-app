from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contact_list')

class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'
    template_name = 'contacts/contact_list.html'
    paginate_by = 10

class ContactDetailView(DetailView):
    model = Contact
    context_object_name = 'contact'
    template_name = 'contacts/contact_detail.html'

class ContactCreateView(SuccessMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/contact_form.html'
    success_url = reverse_lazy('contacts:contact_list')
    success_message = "Contact was created successfully!"

class ContactUpdateView(SuccessMessageMixin, UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/contact_form.html'
    success_url = reverse_lazy('contacts:contact_list')
    success_message = "Contact was updated successfully!"

class ContactDeleteView(SuccessMessageMixin, DeleteView):
    model = Contact
    template_name = 'contacts/contact_confirm_delete.html'
    success_url = reverse_lazy('contacts:contact_list')
    success_message = "Contact was deleted successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

# HTMX Views
def contact_search(request):
    query = request.GET.get('q', '')
    contacts = Contact.objects.filter(name__icontains=query)
    context = {'contacts': contacts}
    return render(request, 'contacts/partials/contact_list_partial.html', context)

