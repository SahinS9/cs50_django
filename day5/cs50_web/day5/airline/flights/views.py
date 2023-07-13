from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.



def index(request):
    return render(request, "flights/index.html", {
        "flights" : Flight.objects.all()
    })
    

def flight(request, flight_id):
    flight = Flight.objects.get(pk = flight_id)
    return render(request, "flights/flight.html",{
                    "flight" : flight  ,
                    "passengers" : flight.passengers.all(),
                    #passengers method here is the name of the related_name in the MODEL       
                    "non_passengers": Passenger.objects.exclude(flights = flight).all()        
                  })

def book(request, flight_id):
    #if we will manipulate db, need to use POST method
    if request.method == "POST":
        flight = Flight.objects.get(pk = flight_id)
        passenger = Passenger.objects.get(pk = int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flight', args = (flight.id,)))
