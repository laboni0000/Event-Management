from django import forms 
from django.forms import ModelForm 
from .models import Venue, Event


class VenueForm(ModelForm):
    class Meta:
        model = Venue 
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
        
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
            
        }
        
        widgets = {
            'name' : forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder': 'Venue Name'}),
            'address' : forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder': 'Address'}),
            'zip_code' : forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder': 'Zip Code'}),
            'phone' : forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder': 'Phone'}),
            'web' : forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder': 'web'}),
            'email_address' : forms.EmailInput(attrs={ 'class' : 'form-control', 'placeholder': 'Email Inputs'}),
        } 


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue',  'attendees', 'description')
        
        labels = {
            'name': '',
            'event_date': 'YYYY-MM-DD  HH:MM:SS',
            'venue': 'Venue',
            'attendees': 'Attendees',
            'email_address': '',
        }
        
        widgets = {
            'name' : forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder': 'Event Name'}),
            'event_date' : forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder': 'Event Date'}),
            'venue' : forms.Select(attrs={ 'class' : 'form-control', 'placeholder': 'Venue'}),
            'attendees' : forms.SelectMultiple(attrs={ 'class' : 'form-control', 'placeholder': 'Attendees'}),
            'description' : forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder': 'Description'}),
        }
        