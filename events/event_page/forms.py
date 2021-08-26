from django import forms
from .models import Event

# create a class form
class EventForm(forms.ModelForm):
    class Meta:
        # get our forms from model fields provided
        model = Event
        fields = ('event_name', 'date', 'time', 'location', 'image')

        # use widgets to style our form tags
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event title'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YY-MM-DD'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Hr:Min:Sec'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event location'}),
        }