from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from mtb.models import Customer, Bike, ContactPerson, Checkin
#from datetime import datetime, timedelta
from django.utils import timezone


# Create your views here.


def customers(request):
    return render_to_response("customers.html",
                              {"customers": Customer.objects.all()})


def bikes(request):
    if request.method == "POST":
        for bike in Bike.objects.all():
            bike.IsTaken = False
            bike.save()

        return redirect("/mtb/bikes/")

    args = {}
    args.update(csrf(request))
    args["bikes"] = Bike.objects.all()

    return render_to_response("bikes.html",
                              args
    )

def status(request):
    visitors_today = 0
    total_visitors = 0
    checkins = Checkin.objects.all()

    for checkin in checkins:
        total_visitors += 1 + checkin.Customers.all().count()
        if (timezone.now().date() - checkin.DateTime.date()).days == 0:
            visitors_today += 1 + checkin.Customers.all().count()

    args = {}
    args["bikes"] = Bike.objects.all()
    args["available_bikes"] = 0
    args["visitors_today"] = visitors_today
    for bike in args["bikes"]:
        if bike.IsTaken is True:
            continue
        args["available_bikes"] += 1

    args["total_visitors"] = total_visitors

    args["bikesTaken"] = [bike for bike in args["bikes"] if bike.IsTaken is False]
    return render_to_response("status.html",
                              args)
