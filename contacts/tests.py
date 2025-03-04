from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import Contact
from .forms import ContactForm

class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name="John Doe",
            email="john@example.com",
            phone_number="1234567890",
            address="123 Main St",
            notes="Test notes"
        )

    def test_contact_creation(self):
        self.assertTrue(isinstance(self.contact, Contact))
        self.assertEqual(str(self.contact), "John Doe")

    def test_contact_fields(self):
        self.assertEqual(self.contact.name, "John Doe")
        self.assertEqual(self.contact.email, "john@example.com")
        self.assertEqual(self.contact.phone_number, "1234567890")
        self.assertEqual(self.contact.address, "123 Main St")
        self.assertEqual(self.contact.notes, "Test notes")

class ContactViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.contact = Contact.objects.create(
            name="John Doe",
            email="john@example.com",
            phone_number="1234567890",
            address="123 Main St"
        )
        self.list_url = reverse('contacts:contact_list')
        self.detail_url = reverse('contacts:contact_detail', args=[self.contact.id])
        self.create_url = reverse('contacts:contact_create')
        self.update_url = reverse('contacts:contact_update', args=[self.contact.id])
        self.delete_url = reverse('contacts:contact_delete', args=[self.contact.id])
        self.search_url = reverse('contacts:contact_search')

    def test_contact_list_view(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contact_list.html')
        self.assertTrue('contacts' in response.context)

    def test_contact_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contact_detail.html')
        self.assertEqual(response.context['contact'], self.contact)

    def test_contact_create_view(self):
        # Test GET request
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contact_form.html')
        
        # Test POST request
        data = {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'phone_number': '0987654321',
            'address': '456 Oak St'
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(Contact.objects.count(), 2)
        self.assertRedirects(response, self.list_url)

    def test_contact_update_view(self):
        data = {
            'name': 'John Updated',
            'email': 'john.updated@example.com',
            'phone_number': '1234567890',
            'address': '123 Main St Updated'
        }
        response = self.client.post(self.update_url, data)
        self.contact.refresh_from_db()
        self.assertEqual(self.contact.name, 'John Updated')
        self.assertEqual(self.contact.email, 'john.updated@example.com')

    def test_contact_delete_view(self):
        response = self.client.post(self.delete_url)
        self.assertEqual(Contact.objects.count(), 0)
        self.assertRedirects(response, self.list_url)

    def test_contact_search_view(self):
        # Test search by name
        response = self.client.get(self.search_url, {'q': 'John'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/partials/contact_list_partial.html')
        self.assertTrue(self.contact in response.context['contacts'])

        # Test search by email
        response = self.client.get(self.search_url, {'q': 'john@example'})
        self.assertTrue(self.contact in response.context['contacts'])

        # Test search by phone
        response = self.client.get(self.search_url, {'q': '1234'})
        self.assertTrue(self.contact in response.context['contacts'])

        # Test search with no results
        response = self.client.get(self.search_url, {'q': 'nonexistent'})
        self.assertEqual(len(response.context['contacts']), 0)

class ContactFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone_number': '1234567890',
            'address': '123 Main St'
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Test empty form
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # name, phone_number, and address are required
        
        # Test invalid email
        data = {
            'name': 'John Doe',
            'email': 'invalid-email',
            'phone_number': '1234567890',
            'address': '123 Main St'
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertTrue('email' in form.errors)

    def test_optional_fields(self):
        data = {
            'name': 'John Doe',
            'phone_number': '1234567890',
            'address': '123 Main St'
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid(), "Form should be valid with only required fields")
