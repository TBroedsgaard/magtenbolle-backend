from django.shortcuts import render_to_response
from mtb.models import Customer

# Create your views here.


def customers(request):
    return render_to_response("customers.html",
                              {"customers": Customer.objects.all()})
