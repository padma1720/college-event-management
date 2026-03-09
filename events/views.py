from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Event, Registration
from django.core.mail import send_mail
from django.conf import settings

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def register_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        Registration.objects.create(event=event, name=name, email=email)
        
        
        send_mail(
            'Event Registration Confirmation',
            f'Hi {name},\nYou have successfully registered for {event.title}.',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return render(request, 'events/thanks.html', {'event': event})
    return render(request, 'events/register.html', {'event': event})

