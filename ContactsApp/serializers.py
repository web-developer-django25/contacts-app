# ContactsApp/serializers.py
from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'  # Or specify fields: ['id', 'name', 'address', ...]