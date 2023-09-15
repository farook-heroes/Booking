from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Booking

# importing HttResponse from library
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello world")




def home(request):
    if request.method=="POST":
        name=request.POST["name"]
        description=request.POST['description']
        phone=request.POST['phone']
        date=request.POST['date']
        booking = Booking(
        name=name,
        phone=phone,
        description=description,
        date=date,)
        booking.save()
        messages.add_message(request, messages.INFO, "booked")
        return redirect("/home")
   
    return render(request,"home.html")