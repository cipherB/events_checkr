from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

#import model
from .models import Event

#import forms
from .forms import EventForm

# Create your views here.

# this function helps toggle the like feature
def like(request, pk):
    # check if object exists and get, if not => send 404 message
    liked = get_object_or_404(Event, id=request.POST.get('event_id'))

    #toggle between like and unlike
    if liked.is_liked == False:
        liked.is_liked = True
        liked.save()
    else:
        liked.is_liked = False
        liked.save()
    return HttpResponseRedirect(reverse('homepage'))

# home page function that displays all events
def home(request):
    # if a post method is called
    if request.method == 'POST':
        # get our post request and any located files in the request
        form = EventForm(request.POST, request.FILES)
        # check if form is valid, if valid then save
        if form.is_valid():
            form.save()
        # instantly redirect to homepage
        return HttpResponseRedirect(reverse('homepage'))
    
    # get all events in database
    events = Event.objects.all().order_by('-id')

    form = EventForm()
    context = {
        'form': form,
        'events': events,
    }

    return render(request, 'home.html', context)

# Function to filter all liked events and display in likes page
def like_page(request):
    # get all liked events
    events = Event.objects.filter(is_liked=True).order_by('-id')
    context = {
        'events': events,
    }

    return render(request, 'like.html', context)

