from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from mtb.models import Customer, Bike

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