from django.conf.urls import patterns, include, url
from mtb.api import CustomerResource, RegistrationResource, ParticipantResource, BikeResource

customer_resource = CustomerResource()
participant_resource = ParticipantResource()
bike_resource = BikeResource()
registration_resource = RegistrationResource()


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        url(r"^customers/$", "mtb.views.customers"),
        url(r"^api/", include(customer_resource.urls)),
        url(r"^api/", include(participant_resource.urls)),
        url(r"^api/", include(bike_resource.urls)),
        url(r"^api/", include(registration_resource.urls)),
)
