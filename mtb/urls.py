from django.conf.urls import patterns, include, url
from mtb.api import ContactPersonResource, CustomerResource, BikeResource, PaymentResource, CheckinResource, DummyResource, DimmyResource

contactperson_resource = ContactPersonResource()
customer_resource = CustomerResource()
bike_resource = BikeResource()
payment_resource = PaymentResource()
checkin_resource = CheckinResource()
dummy_resource = DummyResource()
dimmy_resource = DimmyResource()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        url(r"^$", "mtb.views.status"),
        url(r"^customers/$", "mtb.views.customers"),
        url(r"^bikes/$", "mtb.views.bikes"),
        url(r"^api/", include(contactperson_resource.urls)),
        url(r"^api/", include(customer_resource.urls)),
        url(r"^api/", include(bike_resource.urls)),
        url(r"^api/", include(payment_resource.urls)),
        url(r"^api/", include(checkin_resource.urls)),
        url(r"^api/", include(dummy_resource.urls)),
        url(r"^api/", include(dimmy_resource.urls)),
)
